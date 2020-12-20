class TestService:
    def __init__(self, test_dao):
        self.test_dao = test_dao

    def test_service(self):
        return self.test_dao.get_dao()