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
This Minion is meant to control MPD, the Music Player Daemon.
'''

import os
from intercom.minion2 import Minion

minion = Minion('minion.mpd')


@minion.register('do:mpd.play')
def play(topic, msg):
    os.system('mpc play')


@minion.register('do:mpd.pause')
def pause(topic, msg):
    os.system('mpc pause')


@minion.register('do:mpd.next')
def next(topic, msg):
    os.system('mpc next')


@minion.register('do:mpd.prev')
def prev(topic, msg):
    os.system('mpc prev')


@minion.register('discover.minion')
def discover(topic, msg):
    minion.announce([
        {'type': 'action',
         'label': 'Play',
         'topic': 'do:mpd.play',
         },
        {'type': 'action',
         'label': 'Pause',
         'topic': 'do:mpd.pause',
         },
        ])


if __name__ == '__main__':
    minion.run()
