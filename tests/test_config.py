from unittest import TestCase
import os
import sys
import ConfigParser
import cStringIO
import tempfile
import shutil

import acme
from acme import metadata

__author__ = metadata.authors
__copyright__ = metadata.copyright
__license__ = metadata.license


def setenv(name, value):
    os.environ[name] = value


def unsetenv(name):
    os.environ[name] = ''


class TestConfigFilenames(TestCase):
    def test_get_config_filenames_no_env(self):
        pass

    def test_get_config_filenames_with_XDG_CONFIG_HOME_set(self):
        pass

    def test_get_config_filenames_with_XDG_CONFIG_DIRS_set(self):
        pass

    def test_get_config_filenames_with_XDG_vars_set(self):
        pass

ANSIBLE_DEFAULTS = {'ansible_managed':
                    'This file is managed remotely, all changes will be lost'}


class TestReadConfig(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _make_configfile(self, dir, sect, *data):
        pass

    def _read_config(self, project_dir):
        pass

    def test_read_config_files_simple(self):
        pass

    def test_read_config_files_precedence(self):
        pass

    def test_read_config_files_with_project_root(self):
        pass

    def test_read_config_files_with_project_root_precedence(self):
        pass


class TestReadConfig2(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _make_configfile(self, dir, sect, *data):
        pass

    def _read_config(self, project_dir):
        pass

    def test_defaults(self):
        pass

    def test_read_config_files_simple(self):
        pass


class TestReadConfigDefaultsForPlattforms(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_defaults_linux(self):
        pass

    def test_defaults_windows_without_APPDATA(self):
        pass

    def test_defaults_windows_with_APPDATA(self):
        pass

    def test_defaults_os_x(self):
        pass


