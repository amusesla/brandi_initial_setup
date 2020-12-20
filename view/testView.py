from flask import jsonify

def create_endpoints(app, services):
    test_service = services.test_service

    @app.route('/test', methods=['GET'])
    def test():
        tables = test_service.test_service()
        return jsonify(tables)