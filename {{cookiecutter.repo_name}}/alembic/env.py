"""Alembic migrations."""
from websauna.system.devop import alembic


alembic.run_alembic(package="{{ cookiecutter.repo_name }}")
