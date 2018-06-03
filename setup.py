"""Cookiecutter template to create a Websauna addon."""
from setuptools import setup

import os


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()

requires = [
    'cookiecutter'
]

dev_requirements = [
    'zest.releaser[recommended]'
]

test_requirements = [
    'binaryornot',
    'flake8',
    'pytest',
    'pytest-cookies',
    'sh',
]

setup(
    name='cookiecutter-websauna-addon',
    version='1.0.0a1',
    description='Cookiecutter template to create a Websauna addon.',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
    ],
    keywords=(
        'cookiecutter, Python, projects, project templates, '
        'skeleton, scaffolding, project directory, setup.py'
    ),
    author='Websauna',
    author_email='developers@websauna.org',
    url='https://github.com/websauna/cookiecutter-websauna-addon',
    packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extras_require={
        # Dependencies for preparing releases
        'dev': dev_requirements,
        # Dependencies for running test suite
        'test': test_requirements,
    },
    entry_points="""""",
)
