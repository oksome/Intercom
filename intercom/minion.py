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
    '''
    Sample Minion, prints all the messages it receives.
    Inherit your Minions from this class.
    '''

    def __init__(self, topics, intercom='tcp://relay.intercom:5555'):
        self.topics = topics
        self.intercom = intercom
        self.reset()

    def reset(self):
        'Reset the ZMQ socket connection.'

        # Socket to talk to server
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        print("Collecting updates from server...")
        self.socket.connect(self.intercom)
        for topic in self.topics:
            self.socket.setsockopt(zmq.SUBSCRIBE, bytes(topic, 'utf-8'))

    def run(self):
        'Main event loop.'

        while True:
            string = self.socket.recv()
            topic, messagedata = string.split(b' ', 1)
            topic = str(topic, 'utf-8')
            msg = json.loads(str(messagedata, 'utf-8'))
            self.receive(topic, msg)

    def receive(self, topic, msg):
        'Handles new messages. Override this function with your behaviour.'
        print(topic, msg)


if __name__ == '__main__':

    # Obtaining optional hostname from CLI:
    import sys
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = 'relay.intercom'
    if ':' not in host:
        host += ':5555'


    m = Minion(('',), 'tcp://' + host)
    m.run()
