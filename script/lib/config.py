#!/usr/bin/env python3

from __future__ import print_function
import os
import sys

PLATFORM = {
  'cygwin': 'win32',
  'msys': 'win32',
  'darwin': 'darwin',
  'linux': 'linux',
  'linux2': 'linux',
  'win32': 'win32',
}[sys.platform]

verbose_mode = False


def get_platform_key():
  return 'mas' if 'MAS_BUILD' in os.environ else PLATFORM


def get_target_arch():
  arch = os.environ.get('TARGET_ARCH')
  return 'x64' if arch is None else arch


def enable_verbose_mode():
  print('Running in verbose mode')
  global verbose_mode
  verbose_mode = True


def is_verbose_mode():
  return verbose_mode


def get_zip_name(name, version, suffix=''):
  arch = get_target_arch()
  if arch == 'arm':
    arch += 'v7l'
  zip_name = '{0}-{1}-{2}-{3}'.format(name, version, get_platform_key(), arch)
  if suffix:
    zip_name += f'-{suffix}'
  return f'{zip_name}.zip'
