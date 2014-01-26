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
For suspend to work, you need to:
Add yourself to the 'power' group.
echo "%power    ALL=(ALL) NOPASSWD:/usr/sbin/pm-suspend" >> /etc/sudoers.d/power

'''

import os

from intercom.minion import Minion


class MPDMinion(Minion):
    '''
    This Minion is meant to control MPD, the Music Player Daemon.
    '''

    def __init__(self, topics, intercom):
        super(MPDMinion, self).__init__(topics, intercom)

    def receive(self, topic, msg):
        print(topic, msg)

        if topic == 'do:mpd.play':
            os.system('mpc play')
        if topic == 'do:mpd.pause':
            os.system('mpc pause')
        else:
            print('Unknown topic')
            


if __name__ == '__main__':
    m = MPDMinion(('do:mpd',))
    m.run()
