Acme
====

.. contents::
   :depth: 3
..

|image|

|CII Best Practices|

**Your Linux-based data center in a box**

A collection of `Ansible <https://ansible.com/>`__ playbooks, scalable
from one container to an entire data center.

Acme as a framework
===================

-  **lots of highly extensible roles** with sane defaults
-  **Tuned for production** and works great for development
-  **Built for modularity** so extending it is simple
-  **Custom scripts** to tie everything together

We believe in the \*Nix philosophy; one tool should only do one thing
very well. Acme is building out specialised playboks and roles, but it
is just a set of focused tools to help you run amd manage your
infrastructure.

In fact, you can run all the roles with Ansible directly too.

Installation
============

Dependencies
------------

Acme requires a single dependency that is not installed by Ansible.
Install ``netaddr`` however you see fit:

::

    $ pip install netaddr
    $ apt-get install python-netaddr
    $ yum install python-netaddr

Acme Scripts
------------

The easiest way to install Acme is:

::

    $ sudo pip install acme
    $ acme-update

If you want to have more control on the installation process, you can
use:

::

    $ git clone https://github.com/infrascloudy/acme
    $ sudo pip install acme/
    $ acme-update

Building Acme
=============

As it is an all-in-one solution, the tools used are rather opinionated.
They include:

-  `Paver <http://paver.github.io/paver/>`__ for running miscellaneous
   tasks
-  `Setuptools <http://pythonhosted.org/setuptools/merge.html>`__ for
   distribution (Setuptools and
   `Distribute <http://pythonhosted.org/distribute/>`__ have
   `merged <http://pythonhosted.org/setuptools/merge.html>`__)
-  `Sphinx <http://sphinx-doc.org/>`__ for documentation
-  `flake8 <https://pypi.python.org/pypi/flake8>`__ for source code
   checking
-  `pytest <http://pytest.org/latest/>`__ for unit testing
-  `mock <http://www.voidspace.org.uk/python/mock/>`__ for mocking (not
   required by the template, but included anyway)
-  `tox <http://testrun.org/tox/latest/>`__ for testing on multiple
   Python versions

If you are new to Python or new to creating Python projects, see Kenneth
Reitz's `Hitchhiker's Guide to
Python <http://docs.python-guide.org/en/latest/>`__ for an explanation
of some of the tools used here.

Licenses
--------

The code which makes up this Python project template is licensed under
the MIT/X11 license. Feel free to use it in your free
software/open-source or proprietary projects.

The template also uses a number of other pieces of software, whose
licenses are listed here for convenience. It is your responsibility to
ensure that these licenses are up-to-date for the version of each tool
you are using.

| Project                   | License                             |
|---------------------------|-------------------------------------|
| Python itself             | Python Software Foundation License  |
| argparse (now in stdlib)  | Python Software Foundation License  |
| Sphinx                    | Simplified BSD License              |
| Paver                     | Modified BSD License                |
| colorama                  | Modified BSD License                |
| flake8                    | MIT/X11 License                     |
| mock                      | Modified BSD License                |
| pytest                    | MIT/X11 License                     |
| tox                       | MIT/X11 License                     |

Issues
------

Please report any bugs or requests that you have using the GitHub issue
tracker!

Authors
-------

-  InfrasCloudy
-  Allanice001

.. |image| image:: https://travis-ci.org/infrascloudy/acme.svg?branch=master
   :target: https://travis-ci.org/infrascloudy/acme
.. |CII Best Practices| image:: https://bestpractices.coreinfrastructure.org/projects/237/badge
   :target: https://bestpractices.coreinfrastructure.org/projects/237
