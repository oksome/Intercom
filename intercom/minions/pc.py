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
This Minion is meant to run on a personal computer running Linux or similar.
It can be used to suspend the computer.

For suspend to work, you need to:
echo "%power    ALL=(ALL) NOPASSWD:/usr/sbin/pm-suspend" >> /etc/sudoers.d/power
'''

import os
from intercom.minion import Minion

minion = Minion('minion.pc')


@minion.register('do:pc.suspend')
def suspend(topic, msg):
    print('Suspending...')
    os.system('sudo pm-suspend')


@minion.register('discover.minion')
def discover(topic, msg):
    minion.announce([{
        'type': 'action',
        'label': 'Suspend',
        'topic': 'do:pc.suspend',
        }])


if __name__ == '__main__':
    minion.run()
