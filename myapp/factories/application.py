import os

from flask import Flask

from myapp.controllers import home
from myapp.factories.configuration import Config


def create_application() -> Flask:
    """
    Basic application configuration
    :return: Flask App instance
    """
    app = Flask(__name__,
                template_folder=os.path.join(Config.MODULE_DIR, 'templates'))
    app.config.from_object(Config)
    app.register_blueprint(home)
    return app
