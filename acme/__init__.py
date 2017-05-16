# -*- coding: utf-8 -*-
"""It does cool things to servers with the help of Ansible"""
from __future__ import print_function

import os
import subprocess
import stat
try:
    from shlex import quote as shquote
except ImportError:
    def shquote(s):
        if not s:
            return "''"
        return "'" + s.replace("'", "'\"'\"'") + "'"

from acme import metadata
from acme.config import ACME_CONFIG

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
ENCFS_CONFIGFILE = ".encfs6.xml"
ENCFS_PREFIX = ".encfs."
SECRET_NAME = "secret"

ENCFS_KEYFILE = ".encfs6.keyfile"
ENCFS_KEYFILE_LENGTH = 256


def _find_up(path, name):
    path = os.path.abspath(path)
    last = None
    while path != last:
        last = path
        path = os.path.join(path, name)
        if os.path.exists(path):
            return path
        path = os.path.dirname(last)
    return None


def find_acme_project(path=None):
    if path is None:
        path = os.getcwd()
    acme_config = _find_up(path, ACME_CONFIG)
    return os.path.dirname(acme_config) if acme_config else None


def find_playbookpath(config, project_root):
    if project_root:
        places = [os.path.join(project_root, "acme-playbooks", "playbooks")]
    else:
        places = []
    places.extend(config['paths']['playbooks-paths'])
    for playbook_path in places:
        if os.path.exists(os.path.join(playbook_path, "site.yml")):
            return playbook_path


def find_inventorypath(project_root):
    for inventory_path in ANSIBLE_INVENTORY_PATHS:
        ansible_inventory = os.path.join(project_root, inventory_path)
        if os.path.isdir(ansible_inventory):
            return ansible_inventory


def padlock_lock(encrypted_path):
    decrypted_path = ''.join(encrypted_path.rsplit(ENCFS_PREFIX, 1))
    if not os.path.ismount(decrypted_path):
        return False
    subprocess.call(['fusermount', '-u', decrypted_path])
    return True


def padlock_unlock(encrypted_path):
    keyfile = os.path.join(encrypted_path, ENCFS_KEYFILE)
    configfile = os.path.join(encrypted_path, ENCFS_CONFIGFILE)
    crypted_configfile = configfile + '.asc'

    if (not os.path.exists(keyfile) or
            not os.path.exists(crypted_configfile)):
        return False

    decrypted_path = ''.join(encrypted_path.rsplit(ENCFS_PREFIX, 1))

    if os.path.ismount(decrypted_path):
        return False

    if not os.path.isdir(decrypted_path):
        os.makedirs(decrypted_path)

    if not os.path.exists(configfile):
        os.mkfifo(configfile)
    elif not stat.S_ISFIFO(os.stat(configfile).st_mode):
        raise IOError(17, configfile + ' exists but is not a fifo')

    encfs = subprocess.Popen([
        'encfs', encrypted_path, decrypted_path,
        '--extpass', 'gpg --no-mdc-warning --output - %s' % shquote(keyfile)])

    with open(configfile, 'w') as fh:
        subprocess.Popen(['gpg', '--no-mdc-warning', '--output', '-', crypted_configfile], stdout=fh).wait()

    encfs.wait()
    os.remove(configfile)
    return True
