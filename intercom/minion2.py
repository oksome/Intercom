# Copyright (c) 2013 "OKso http://okso.me"
#
# This file is part of Intercom.
#
# Intercom is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# DESIGNED FOR Python 3

'''
A Minion is an network endnode, connected to some input/output gadgets.
'''

import zmq
import json


class Minion:

    def __init__(self, name):
        self._name = name
        self._registrations = {}

    def register(self, topic):
        def decorator(function):
            if topic in self._registrations:
                self._registrations[topic].append(function)
            else:
                self._registrations[topic] = [function]
        return decorator

    def setup(self, relay):
        # Socket to talk to server
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.socket.connect(relay)
        for topic in self._registrations:
            self.socket.setsockopt(zmq.SUBSCRIBE, bytes(topic, 'utf-8'))

    def receive(self, topic, msg):
        for t in self._registrations:
            if t.startswith(topic):
                for f in self._registrations[t]:
                    f(topic, msg)

    def send(self, topic, msg):
        if type(topic) != bytes:
            topic = bytes(str(topic), 'utf-8')
        messagedata = bytes(json.dumps(msg), 'utf-8')

        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect(self._relay_in)
        socket.send(topic + b' ' + messagedata)
        reply = socket.recv()
        assert reply

    def announce(self, capabilities):
        msg = {
            'name': self._name,
        }
        msg.update(capabilities)
        self.send('announce.minion', msg)

    def run(self,
            relay_out='tcp://relay.intercom:5555',
            relay_in='tcp://relay.intercom:5556'):
        self.setup(relay_out)
        self._relay_in = relay_in

        while True:
            string = self.socket.recv()
            topic, messagedata = string.split(b' ', 1)
            topic = str(topic, 'utf-8')
            msg = json.loads(str(messagedata, 'utf-8'))
            self.receive(topic, msg)