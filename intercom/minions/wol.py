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
WOL Minion: Wake On LAN other connected devices.
'''

import socket
import struct

from intercom.minion import Minion


class WOLMinion(Minion):
    '''
    This Minion is meant to run on a personal computer running Linux or similar.
    It can be used to suspend the computer.
    '''

    def receive(self, topic, msg):
        print(topic, msg)
        if topic == 'do:net.wol':
            print('Awaking...')
            mac_address = msg['mac'].replace(':', '')
            data = b'FFFFFFFFFFFF' + (mac_address * 20).encode()

            send_data = b''

            # Split up the hex values in pack
            for i in range(0, len(data), 2):
                send_data += struct.pack('B', int(data[i: i + 2], 16))

            # Broadcast it to the LAN.
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.sendto(send_data, ('<broadcast>', 7))

        else:
            print('Unknown topic')
            


if __name__ == '__main__':
    m = WOLMinion(('do:net.wol',))
    m.run()
