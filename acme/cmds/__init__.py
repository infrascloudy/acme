# -*- coding: utf-8 -*-
"""
Support functions for command line utilities (scripts).
"""
from __future__ import print_function

import os
import sys
import platform
import subprocess
try:
    from subprocess import DEVNULL
except ImportError:
    DEVNULL = os.open((os.devnull, os.O_RDWR))

from acme import find_acme_project as _find_acme_project
from acme import find_playbookpath as _find_playbookpath
from acme import find_inventorypath as _find_inventorypath

SCRIPT_NAME = os.path.basename(sys.argv[0])

INSECURE = bool(os.environ.get('INSECURE', False))


def error_msg(message, severity="Error"):
    print(SCRIPT_NAME + ':', severity + ':', message)
    if severity == "Error":
        raise SystemExit(1)


def require_commands(*cmd_names):
    def command_exists(cmd_name):
        which = "where" if platform.system() == "Windows" else "which"
        return not subprocess.call([which, cmd_name],
                                   stdout=DEVNULL, stderr=subprocess.STDOUT)

    for name in cmd_names:
        if not command_exists(name):
            error_msg("%s: command not found" % name)


def find_acme_project(path=None, required=True):
    project_root = _find_acme_project(path)
    if required and not project_root:
        error_msg("Not an Acme project directory")
    return project_root


def find_playbook_path(config, project_root, required=True):
    playbooks_path = _find_playbookpath(config, project_root)
    if required and not playbooks_path:
        error_msg("Acme playbooks not installed")
    return playbooks_path


def find_inventorypath(project_root, required=True):
    inventory = _find_inventorypath(project_root)
    if required and not inventory:
        error_msg("Ansible inventory not found")
    return inventory
