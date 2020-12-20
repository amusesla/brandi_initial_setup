import pymysql

from flask      import Flask
from flask_cors import CORS

from model       import TestDao
from service     import TestService
from view        import create_endpoints

# for getting multiple service classes
class Services:
    pass

def create_app(test_config=None):
    app       = Flask(__name__)
    app.debug = True

    # By default, submission of cookies across domains is disabled due to the security implications.
    CORS(app, resources={r'*': {'origins': '*'}})

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    db         = app.config['DB']
    connection = pymysql.connect(host=db['host'],
                                 user=db['user'],
                                 password=db['password'],
                                 db=db['name'],
                                 charset=db['charset'])

    ## persistence Layer
    test_dao = TestDao(connection)

    ## business Layer
    services = Services
    services.test_service = TestService(test_dao)

    ## create endpoint
    create_endpoints(app, services)

    return app