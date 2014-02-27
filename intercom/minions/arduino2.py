# Copyright (c) 2014 "OKso http://okso.me"
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

import serial
import json
import threading
from intercom.minion import Minion


def connect_arduino():
    for path in ('/dev/ttyUSB0',
                 '/dev/ttyUSB1',
                 '/dev/tty.usbserial-A8008KAi'):
        try:
            return serial.Serial(path, 115200)
        except serial.serialutil.SerialException:
            pass  # Only accept that exception class
    raise serial.serialutil.SerialException(
        "could not open any predefined port")


def arduino_to_intercom(arduino, minion):
    print('start')
    while True:
        line = arduino.readline().strip()
        try:
            result = json.loads(line.decode())
            print('LINE', result)
            minion.send('sensor.weather', result)
        except ValueError:
            print('Mismatch in ', line)

# ===== Minion code =====

arduino = connect_arduino()
minion = Minion('minion.arduino')
minion.setup()

thread = threading.Thread(target=arduino_to_intercom, args=(arduino, minion))
thread.start()


@minion.register('do:arduino.switch')
def switch(topic, msg):
    print('plop')


if __name__ == '__main__':
    minion.run()
