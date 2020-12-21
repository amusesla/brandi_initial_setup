from flask import jsonify, request
from flask.views import MethodView
from connection import get_connection


class HealthCheckView(MethodView):
    def __init__(self, service, database):
        self.service = service
        self.database = database

    def get(self):
        connection = get_connection(self.database)
        tables = self.service.get_health_check_service(connection)
        connection.close()
        return jsonify(tables)

    def post(self):
        data = request.json
        connection = get_connection(self.database)
        menus = self.service.post_health_check_service(connection, data)
        connection.close()
        return jsonify(menus)