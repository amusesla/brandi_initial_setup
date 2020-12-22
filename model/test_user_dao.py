import pymysql
class TestUserDao:

    def get_dao(self, connection, user_id):
        user_id = user_id

        """
        GET 메소드: 유저 정보 조회

        Args:
            connection: 데이터베이스 연결 객체
            user_id      : 서비스에서 넘겨 받은 수정할 user 의 id

        Author: 홍길동

        Returns:
            200, { 해당 유저 정보 } : 조회 성공
            400, {'errorMessage': 'user_does_not_exist'} : 유저 정보 조회 실패


        History:
            2020-20-20(홍길동): 초기 생성
            2020-20-21(홍길동): 1차 수정
            2020-20-22(홍길동): 2차 수정

        Raises:
        """
        sql ="""
            SELECT * 
            FROM users
            WHERE id=%s;
        """

        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
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

        """
        POST 메소드: 유저 정보 생성

        Args:
            connection: 데이터베이스 연결 객체
            name      : 생성할 user의 name
            gender    : 생성할 user의 gender
            age       : 생성할 user의 age

        Author: 홍길동

        Returns:
            200, {'message': 'success'} : 생성 성공
            400, {'errorMessage': 'unable_to_create'} : 유저 생성 실패


        History:
            2020-20-20(홍길동): 초기 생성
            2020-20-21(홍길동): 1차 수정
            2020-20-22(홍길동): 2차 수정

        Raises:
        """
        sql ="""
        INSERT INTO users 
        (
            name,
            gender,
            age
        )
        VALUES(
            %(name)s,
            %(gender)s,
            %(age)s
            );
        """


        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql, (
                params
            ))
            result = cursor.lastrowid
            if not result:
                raise Exception('unable_to_create')
            return result

    def patch_dao(self, connection, user_id, age):
        params = dict()
        params['user_id'] = user_id
        params['age'] = age
        """
        PATCH 메소드: 유저 정보 수정

        Args:
            connection: 데이터베이스 연결 객체
            user_id   : 수정할 user 의 id
            age       : 수정할 user 의 age

        Author: 홍길동

        Returns:
            200, {'message': 'success'} : 수정 성공
            400, {'errorMessage': 'unable_to_update'} : 유저 수정 실패


        History:
            2020-20-20(홍길동): 초기 생성
            2020-20-21(홍길동): 1차 수정
            2020-20-22(홍길동): 2차 수정

        Raises:
        """

        sql = """
        UPDATE users 
        SET age =%s 
        WHERE id=%s;
        """

        with connection.cursor() as cursor:
            affected_row = cursor.execute(sql, (
                params
            ))
            if affected_row == 0:
                raise Exception('unable_to_update')
