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

import intercom.broker as broker


def test_broker_init():
    r = broker.Broker()
    assert r


def test_broker_reset():
    r = broker.Broker()
    assert r
    #r.reset()


def test_get_ips():
    ip = broker.get_ips()
    assert ip


def test_announcer_init():
    a = broker.Announcer()
    assert a


def test_announcer_run():
    magic = broker.ANNOUNCE_MAGIC
    try:
        broker.ANNOUNCE_MAGIC = 'PYTEST'
        a = broker.Announcer()
        a.start()
        a.stop()
    finally:
        broker.ANNOUNCE_MAGIC = magic


def test_without_netifaces():
    if broker.ni:
        ni = broker.ni
        broker.ni = None
        try:
            a = broker.Announcer()
            assert a
        finally:
            broker.ni = ni
