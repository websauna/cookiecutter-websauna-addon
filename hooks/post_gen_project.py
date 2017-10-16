"""Create virtualenv and print a thank you note."""
from textwrap import dedent

import subprocess
import sys


try:
    import venv
    VIRTUALENV_AVAILABLE = True
except ImportError:
    VIRTUALENV_AVAILABLE = False


if VIRTUALENV_AVAILABLE:
    try:
        venv.create('env', with_pip=True)
        proc = subprocess.Popen(
            ['env/bin/pip', 'install', '-r', 'requirements.txt'],
            shell=sys.platform.startswith('win'),
            cwd='.'
        )
        print("the commandline is {}".format(proc.args))
        proc.wait()
    except subprocess.CalledProcessError:
        print('It was not possible to create the virtualenv. Maybe inside tox?')
    except FileNotFoundError:
        print(subprocess.check_output(['ls']))


msg = dedent("""
    ===============================================================================
    Websauna Addon.
    Package {{ cookiecutter.repo_name }} was generated.
    Now, code it, create a git repository, push to your Github account.
    Sorry for the convenience.
    ===============================================================================
""")

print(msg)
