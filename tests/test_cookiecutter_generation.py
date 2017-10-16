"""Test cookiecutter generation."""
from binaryornot.check import is_binary

import os
import pytest
import re
import sh


PATTERN = '{{(\s?cookiecutter)[.](.*?)}}'
RE_OBJ = re.compile(PATTERN)


@pytest.fixture
def context():
    """."""
    return {
        'full_name': 'Websauna Team',
        'email': 'developers@websauna.org',
        'company': 'Websauna',
        'github_username': 'websauna',
        'project_name': 'Websauna: News addon',
        'project_short_description': 'Addon for news content with Websauna.',
        'tags': 'python package websauna pyramid',
        'repo_name': 'websauna.news',
        'namespace': 'websauna',
        'package_name': 'news',
        'release_date': 'today',
        'year': '2017',
        'version': '1.0.0a1',
        'authentication_random': '6c613c8193060d3738ca90103a6c79878150220b',
        'authomatic_random': 'dc999820aa1e1b71b166039f7f3cc8cee61567e0',
        'session_random': '42a8a98f766b8eba77a6326a579ecdf6d22b14b7',
    }


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths):
    """Check all paths have correct substitutions."""
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(path) or ('/env/' in path):
            continue
        for line in open(path, 'r'):
            match = RE_OBJ.search(line)
            msg = 'cookiecutter variable not replaced in {0}'
            assert match is None, msg.format(path)


def test_default_configuration(cookies, context):
    """Generated project should replace all variables."""
    result = cookies.bake(extra_context=context)
    assert result.exception is None
    assert result.exit_code == 0
    assert result.project.basename == context['repo_name']
    assert result.project.isdir()

    paths = build_files_list(str(result.project))
    assert paths
    check_paths(paths)


def test_flake8_compliance(cookies):
    """Generated project should pass flake8."""
    result = cookies.bake()
    base_path = str(result.project)
    paths = ['setup.py', 'src']
    for path in paths:
        try:
            sh.flake8('{0}/{1}'.format(base_path, path))
        except sh.ErrorReturnCode as e:
            pytest.fail(e)


def test_generated_package(cookies):
    """Generated project should pass test execution."""
    result = cookies.bake()
    base_path = str(result.project)
    try:
        sh.pytest('{0}/tests'.format(base_path))
    except sh.ErrorReturnCode as e:
        pytest.fail(e)
