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

import intercom.relay as relay

def test_relay_init():
    r = relay.Relay()
    assert r

def test_relay_reset():
    r = relay.Relay()
    #r.reset()

def test_get_ips():
    ip = relay.get_ips()
    assert ip

def test_announcer_init():
    a = relay.Announcer()

def test_announcer_run():
    magic = relay.ANNOUNCE_MAGIC
    try:
        relay.ANNOUNCE_MAGIC = 'PYTEST'
        a = relay.Announcer()
        a.start()
        a.stop()
    finally:
        relay.ANNOUNCE_MAGIC = magic

def test_without_netifaces():
    if relay.ni:
        ni = relay.ni
        relay.ni = None
        try:
            a = relay.Announcer()
        finally:
            relay.ni = ni
