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
The Relay lets Controllers and Minions talk to each other.
'''

import zmq


class Relay:

    def __init__(self):
        self.reset()

    def reset(self):
        context = zmq.Context(1)

        # Socket facing clients
        self.frontend = context.socket(zmq.REP)
        self.frontend.bind("tcp://*:5556")

        # Socket facing services
        self.backend = context.socket(zmq.PUB)
        self.backend.bind("tcp://*:5555")

    def run(self):
        while True:
            msg = self.frontend.recv()
            print('msg', msg)
            self.frontend.send(b'ACK')
            self.backend.send(msg)

if __name__ == '__main__':
    i = Relay()
    i.run()
