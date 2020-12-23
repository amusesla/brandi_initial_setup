from .test_user_view import TestUserView
from error_handler import error_handle


def create_endpoints(app, services, database):
    test_user_service = services.test_user_service

# The arguments passed to as_view() are forwarded to the constructor of the class.
    app.add_url_rule('/test', view_func=TestUserView.as_view('test_user_view', test_user_service, database))

    error_handle(app)
