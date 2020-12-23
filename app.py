from flask import Flask
from flask_cors import CORS

from model import TestUserDao
from service import TestUserService
from view import create_endpoints


# for getting multiple service classes
class Services:
    pass


def create_app(test_config=None):
    app=  Flask(__name__)
    app.debug = True

    # By default, submission of cookies across domains is disabled due to the security implications.
    CORS(app, resources={r'*': {'origins': '*'}})

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    database = app.config['DB']
    # persistence Layer
    test_user_dao = TestUserDao()

    # business Layer
    services = Services
    services.test_user_service = TestUserService(test_user_dao)

    # presentation Layer
    create_endpoints(app, services, database)

    return app
