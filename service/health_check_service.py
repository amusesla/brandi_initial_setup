class HealthCheckService:
    def __init__(self, health_check_dao):
        self.health_check_dao = health_check_dao

    def get_health_check_service(self, database):
        return self.health_check_dao.get_dao(database)

    def post_health_check_service(self, database, data):
        name = data['name']
        menu_id = 2
        return self.health_check_dao.post_dao(database, name, menu_id)