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
Minions can have complex behaviors and functions. This test only attemps at
importing them for a first check.
'''


def test_import_acc():
    import intercom.minions.acc as target
    assert target.minion


def test_import_arduino():
    import intercom.minions.arduino as target
    assert target


def test_import_mpd_minion():
    import intercom.minions.mpd_minion as target
    assert target.minion


def test_import_pc():
    import intercom.minions.pc as target
    assert target.minion


def test_import_pc_with_class():
    import intercom.minions.pc_with_class as target
    assert target


def test_import_tts_espeark():
    import intercom.minions.tts_espeak as target
    assert target.minion


def test_import_wol():
    import intercom.minions.wol as target
    assert target.minion
