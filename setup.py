#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# file: $Id$
# auth: metagriffin <mg.github@uberdev.org>
# date: 2013/11/11
# copy: (C) CopyLoose 2013-EOT metagriffin, see LICENSE.txt
#------------------------------------------------------------------------------
# This software is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.
#------------------------------------------------------------------------------

import os, sys, setuptools
from setuptools import setup, find_packages

# require python 2.7+
if sys.hexversion < 0x02070000:
  raise RuntimeError('This package requires python 2.7 or better')

heredir = os.path.abspath(os.path.dirname(__file__))
def read(*parts, **kw):
  try:    return open(os.path.join(heredir, *parts)).read()
  except: return kw.get('default', '')

test_dependencies = [
  'nose                 >= 1.3.0',
  'coverage             >= 3.5.3',
  ]

dependencies = [
  'distribute           >= 0.6.24',
  ]

entrypoints = None

classifiers = [
  'Development Status :: 1 - Planning',
  #'Development Status :: 2 - Pre-Alpha',
  #'Development Status :: 3 - Alpha',
  #'Development Status :: 4 - Beta',
  #'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'Operating System :: OS Independent',
  'Natural Language :: English',
  'Environment :: Plugins',
  'Framework :: Pyramid',
  'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
  'Topic :: Security',
  'Topic :: Software Development :: Libraries :: Python Modules',
  'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
  ]

setup(
  name                  = 'secpass_controller',
  version               = read('VERSION.txt', default='0.0.1').strip(),
  description           = 'A Pyramid plugin that implements the SecPass Broker Protocol.',
  long_description      = read('README.rst'),
  classifiers           = classifiers,
  author                = 'metagriffin',
  author_email          = 'mg.pypi@uberdev.org',
  url                   = 'http://github.com/metagriffin/secpass-controller',
  keywords              = 'secpass secure password manager broker protocol pyramid controller',
  packages              = find_packages(),
  platforms             = ['any'],
  include_package_data  = True,
  zip_safe              = True,
  install_requires      = dependencies,
  tests_require         = test_dependencies,
  test_suite            = 'secpass_controller',
  entry_points          = entrypoints,
  license               = 'GPLv3+',
  )

#------------------------------------------------------------------------------
# end of $Id$
#------------------------------------------------------------------------------
