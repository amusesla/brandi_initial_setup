from .test_user_view import TestUserView
from error_handler import error_handle


def create_endpoints(app, services, database):
    test_user_service = services.test_user_service

# ----------------------------------------------------------------------------------------------------------------------
# Service Section(write your code under your name)
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# 김기용 like this
# ----------------------------------------------------------------------------------------------------------------------
    app.add_url_rule('/test', view_func=TestUserView.as_view('test_user_view', test_user_service, database))

# ----------------------------------------------------------------------------------------------------------------------
# 김민구 like this
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Admin 1 Section
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Admin 2 Section
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
    # don't touch this
    error_handle(app)
# ----------------------------------------------------------------------------------------------------------------------
