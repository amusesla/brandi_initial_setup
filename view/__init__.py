def create_endpoints(app, services, database):
    test_service = services.test_service

    app.add_url_rule('/test', view_func=TestView.as_view('test_service'))