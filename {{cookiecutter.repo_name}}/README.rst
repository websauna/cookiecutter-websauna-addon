{{ cookiecutter.project_name }}
================================

This is a Python package for {{ cookiecutter.repo_name }}, an addon for `Websauna framework <https://websauna.org>`_.

To run this package you need Python 3.4+, PostgresSQL and Redis.

Installation
============

Local development mode
-----------------------

Activate the virtual environment of your Websauna application.

Then::

    cd {{ cookiecutter.repo_name }}  # This is the folder with setup.py file
    pip install -e .

Running the development website
===============================

Local development machine
-------------------------

Example (OSX / Homebrew)::

    psql create {{ cookiecutter.package_name }}_dev
    ws-sync-db {{ cookiecutter.repo_name }}/conf/development.ini
    ws-pserve {{ cookiecutter.repo_name }}/conf/development.ini --reload

Running the test suite
======================

First create test database::

    # Create database used for unit testing
    psql create {{ cookiecutter.package_name }}_test

Install test and dev dependencies (run in the folder with ``setup.py``)::

    pip install -e ".[dev,test]"

Run test suite using py.test running::

    py.test

More information
================

Please see https://websauna.org/
