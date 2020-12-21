class HealthCheckDao:

    def get_dao(self, database):
        cursor = database.cursor()
        sql= 'show tables;'

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def post_dao(self, database, name, menu_id):
        cursor = database.cursor()
        sql = 'INSERT INTO menus(id, name) VALUES (%s, %s);'
        menu_list = [menu_id, name]
        cursor.execute(sql, menu_list)
        database.commit()
        row = cursor.lastrowid

        return row, 200
