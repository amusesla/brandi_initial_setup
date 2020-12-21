class TestDao:

    def get_dao(self, database):
        cursor = database.cursor()
        sql    = 'show tables;'

        cursor.execute(sql)
        result = cursor.fetchall()

        return result
