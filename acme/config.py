# -*- coding: utf-8 -*-

import os
import sys
import cStringIO
import ConfigParser

__all__ = ['ACME_CONFIG', 'read_config']

ACME_CONFIG = ".acme.cfg"

DEFAULTS = """
[paths]
data-home: $XDG_DATA_HOME/acme

# Default installation directory
install-path: %(data-home)s/acme-playbooks

# Locations where Acme playbooks might be found
# This MUST be a multi-line string to make ConfigParser work
playbooks-paths: %(install-path)s/playbooks

[ansible defaults]
ansible_managed = This file is managed remotely, all changes will be lost
"""

if sys.platform.startswith('win'):
    DEFAULTS = DEFAULTS.replace('$XDG_DATA_HOME', os.getenv('APPDATA') or '~\\Application Data')
elif sys.platform == 'darwin':  # Mac OS X
    DEFAULTS = DEFAULTS.replace('$XDG_DATA_HOME', '~/Library/Application Support')


def _set_xdg_defaults():
    for name, default in (('XDG_CONFIG_HOME', '~/.config'), ('XDG_CONFIG_DIRS', '/etc/xdg'), ('XDG_DATA_HOME', '~/.local/share')):
        if not os.environ.get(name):
            os.environ[name] = default


def _get_config_filenames():
    if sys.platform.startswith('win'):
        configdirs = [os.getenv('APPDATA')
                      or os.path.expanduser('~\\Application Data')]
    elif sys.platform == 'darwin':  # Mac OS X
        configdirs = [os.path.expanduser('~/Library/Application Support'),
                      '/etc']
        configdirs.reverse()
    else:
        _set_xdg_defaults()
        configdirs = ([os.getenv('XDG_CONFIG_HOME')] +
                      os.getenv('XDG_CONFIG_DIRS').split(':') +
                      ['/etc'])
        configdirs = [os.path.expanduser(d) for d in configdirs]
        configdirs.reverse()
    return [os.path.join(d, 'acme.cfg') for d in configdirs]

_configfiles = _get_config_filenames()


def _expandpath(path):
    return os.path.expanduser(os.path.expandvars(path.strip()))


def read_config(project_root):
    if project_root is None:
        config_files = _configfiles
    else:
        config_files = _configfiles + [os.path.join(project_root, ACME_CONFIG)]
    cfgparser = ConfigParser.SafeConfigParser()
    cfgparser.readfp(cStringIO.StringIO(DEFAULTS))

    try:
        cfgparser.read(config_files)
    except ConfigParser.Error, e:
        raise SystemExit('Error in %s: %s' % (ACME_CONFIG, str(e)))

    cfg = dict((sect, dict(cfgparser.items(sect))) for sect in cfgparser.sections())

    for name in ('data-home', 'install-path'):
        cfg['paths'][name] = _expandpath(cfg['paths'][name])
    cfg['paths']['playbooks-paths'] = [_expandpath(p) for p in cfg['paths']['playbook-paths'].splitlines() if p.strip()]

    return cfg
