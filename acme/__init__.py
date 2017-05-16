# -*- coding: utf-8 -*-
"""It does cool things to servers with the help of Ansible"""
from __future__ import print_function

import os
import subprocess
import stat
import ConfigParser
try:
    from shlex import quote as shquote
except ImportError:
    def shquote(s):
        if not s:
            return "''"
        return "'" + s.replace("'", "'\"'\"'") + "'"

from acme.config import _set_xdg_defaults, _get_config_filenames, _expandpath, read_config

from acme import metadata


__version__ = metadata.version
__author__ = metadata.authors[0]
__license__ = metadata.license
__copyright__ = metadata.copyright

ANSIBLE_CONFIG_FILE = "ansible.cfg"

ROLE_PREFIX = "acme"
ACME_SITE_PLAYBOOK = os.path.join("playbooks", "site.yml")
INVENTORY = "inventory"

ANSIBLE_INVENTORY_PATHS = [
    os.path.join("ansible", INVENTORY),
    INVENTORY]

PADLOCK_CMD = "padlock"



