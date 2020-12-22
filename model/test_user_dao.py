import pymysql
class TestUserDao:

    def get_dao(self, connection, id):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = 'SELECT * FROM users WHERE id=%s;'
            user_id = id
            cursor.execute(sql, user_id)
            result = cursor.fetchall()
            if not result:
                raise Exception('user_does_not_exist')
            return result

    def post_dao(self, connection, name, gender, age):
        params = dict()
        params['name'] = name
        params['gender'] = gender
        params['age'] = age
        sql = 'INSERT INTO users (name, gender, age) VALUES (%(name)s, %(gender)s, %(age)s);'
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql, (
                params
            ))
            result = cursor.lastrowid
            if not result:
                raise Exception('user_does_not_exist')
            return result

    def patch_dao(self, connection, gender, age):
        with connection.cursor() as cursor:
            sql = 'UPDATE users SET age =%s WHERE id=%s;'
            data_list = [age, gender]
            affected_row = cursor.execute(sql, data_list)
            if affected_row == 0:
                raise Exception('unable_to_update')
