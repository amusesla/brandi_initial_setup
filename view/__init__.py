from .health_check_view import HealthCheckView


def create_endpoints(app, services, database):
    test_service = services.health_check_service

    app.add_url_rule('/test', view_func=HealthCheckView.as_view('test_service', test_service, database))