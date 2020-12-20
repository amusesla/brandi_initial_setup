class TestDao:
    def __init__(self, database):
        self.db = database

    def get_dao(self):
        cursor = self.db.cursor()
        sql    = 'show tables;'

        cursor.execute(sql)
        result = cursor.fetchall()

        return result