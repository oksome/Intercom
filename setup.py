#!/usr/bin/env python3
# -*- coding:Utf-8 -*-

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

from setuptools import setup


setup(name='Intercom',
      version='0.1',
      description='Messaging system for Home automation',
      author='OKso.me',
      author_email='@okso.me',
      url='https://github.com/oksome/Intercom/',
      packages=['intercom'],
      install_requires=['pyzmq'],
      license='AGPLv3',
      keywords="home automation zeromq intercom",
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: Console',
                   'Programming Language :: Python',
                   'Operating System :: POSIX',
                   'Operating System :: MacOS :: MacOS X',
                   'Intended Audience :: End Users/Desktop',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Manufacturing',
                   'License :: OSI Approved :: GNU Affero General Public License v3',
                   'Topic :: Home Automation',
                   ],
      )
