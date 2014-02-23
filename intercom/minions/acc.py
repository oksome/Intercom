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
This Minion is meant to control things from accelerometer data.
'''

import os
from intercom.minion2 import Minion

#from mpd import MPDClient
#mpc = MPDClient()
#mpc.connect("ra.ion", 6600)
import socket
s = socket.socket()
s.connect(('ra.ion', 6600))


def mpdControl(measure):
    x, y, z = measure['x'], measure['y'], measure['z']
    x2 = 64 - x
    #print('V', x2)
    if x2 > 0:
        # command = 'mpc volume {}'.format(int(x2 * 1.5))
        #print('LOL: [{}]'.format(command))
        # os.system(command)
        #mpc.setvol(int(x2 * 1.5))
        s.send('setvol {}\n'.format(int(x2 * 1.5)).encode('utf-8'))

minion = Minion('minion.mpd')


@minion.register('sensor:accelerometer')
def accelerometer(topic, msg):
    values = msg['values']
    mpdControl(values)


if __name__ == '__main__':
    minion.run()
