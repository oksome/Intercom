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
A Controller sends commands to Minions via the Intercom.
'''

import os
import time

from intercom.controller import dump, Controller


class KeystrokesController(Controller):

    def do(self, group, plug, action):
        topic = 'do:arduino.switch'

        msg = {'origin': self.name,
               'group': group,
               'plug': plug,
               'action': action,
               }

        self.send(topic, msg)


def main(screen):
    curses.noecho()
    controller = KeystrokesController(os.uname().nodename + '/keystrokes', 'tcp://' + host)
    codes = {'k': ('00011', '10000', 'on'),
             'l': ('00011', '10000', 'off'),
             'b': ('00001', '10000', 'on'),
             'n': ('00001', '10000', 'off'),
             }
    while 1:
        c = screen.getch()
        cc = chr(c)
        screen.addstr(2, 2, str([c]))

        if cc in codes:
            controller.do(*codes[cc])
        elif cc == 'q':
            break
        else:
            screen.addstr(4, 2, 'Unknown')
        

    curses.endwin()

if __name__ == '__main__':
    
    # Obtaining optional hostname from CLI:
    import sys
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = 'localhost'
    if ':' not in host:
        host += ':5556'

    import curses
    curses.wrapper(main)
