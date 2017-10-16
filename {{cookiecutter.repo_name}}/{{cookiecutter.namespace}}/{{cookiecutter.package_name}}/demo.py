"""This contains app entry point for running a demo site or functional tests for this addon."""
import websauna.system


class Initializer(websauna.system.DemoInitializer):
    """A demo / test app initializer for testing addon {{ cookiecutter.repo_name }}."""

    def include_addons(self):
        """Include this addon in the configuration."""
        self.config.include("{{ cookiecutter.repo_name }}")


def main(global_config, **settings):
    init = Initializer(global_config)
    init.run()
    return init.make_wsgi_app()
