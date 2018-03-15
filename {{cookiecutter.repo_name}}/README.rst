{{ cookiecutter.project_name }}
================================

This is a Python package for {{ cookiecutter.repo_name }}, an addon for `Websauna framework <https://websauna.org>`_.

To run this package you need Python 3.4+, PostgresSQL and Redis.


Installation
============

Local development mode
-----------------------

Activate the virtual environment of your Websauna application.

Then

    .. code-block:: shell

        cd {{ cookiecutter.repo_name }}  # This is the folder with setup.py file
        pip install -e .  # Install this package


Running the development website
===============================

Local development machine
-------------------------

Create the database:

    .. code-block:: shell

        psql create {{ cookiecutter.package_name }}_dev  # Create database


.. note:: Edit the *{{ cookiecutter.namespace }}/{{ cookiecutter.package_name }}/conf/development.ini* file and change the connection string to the
          one used on your environment. i.e.: postgresql://username:passwd@localhost/{{ cookiecutter.package_name }}_dev


Sync models from this application to the newly created database:

    .. code-block:: shell

        ws-sync-db ws://{{ cookiecutter.namespace }}/{{ cookiecutter.package_name }}/conf/development.ini


Add a user with administrative rights:

    .. code-block:: shell

        ws-create-user ws://{{ cookiecutter.namespace }}/{{ cookiecutter.package_name }}/conf/development.ini admin@example.com mypassword


Start the application:

    .. code-block:: shell

        pserve ws://{{ cookiecutter.namespace }}/{{ cookiecutter.package_name }}/conf/development.ini


Running the test suite
======================

First create test database:

    .. code-block:: shell

        # Create database used for unit testing
        psql create {{ cookiecutter.package_name }}_test


Install test and dev dependencies (run in the folder with ``setup.py``):

    .. code-block:: shell

        pip install -e ".[dev,test]"


Run test suite using py.test running:

    .. code-block:: shell

        py.test


More information
================

Please see https://websauna.org/
