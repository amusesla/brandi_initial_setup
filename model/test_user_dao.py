import pymysql
from custom_exceptions import UserUpdateDenied, UserCreateDenied, UserNotExist


class TestUserDao:
    """ Persistence Layer

        Attributes: None

        Author: 홍길동

        History:
            2020-20-20(홍길동): 초기 생성
            2020-20-21(홍길동): 1차 수정
            2020-20-22(홍길동): 2차 수정
    """

    def get_dao(self, connection, user_id):
        user_id = user_id
        """유저 정보 조회

        Args:
            connection: 데이터베이스 연결 객체
            user_id   : 서비스 레이어에서 넘겨 받은 수정할 user_id

        Author: 홍길동

        Returns:
            return [{'id': 12, 'name': '김기용', 'gender': '남자', 'age': '18'}]

        History:
            2020-20-20(홍길동): 초기 생성
            2020-20-21(홍길동): 1차 수정
            2020-20-22(홍길동): 2차 수정
            
        Raises:
            400, {'message': 'user dose not exist', 'errorMessage': 'user_does_not_exist'} : 유저 정보 조회 실패
        """

        sql = """
            SELECT * 
            FROM users
            WHERE id=%s;
        """

        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql, user_id)
            result = cursor.fetchall()
            if not result:
                raise UserNotExist('already_exist')
            return result

    def get_username(self, connection, name):
        username = name
        """유저 이름 중복 검사

        Args:
            connection: 데이터베이스 연결 객체
            name      : 서비스에서 넘겨 받은 수정할 user 유저

        Author: 홍길동

        Returns:
            return ()                                                        : 해당 유저 없음
            return [{'id': 12, 'name': '김기용', 'gender': '남자', 'age': '18'}]: 해당 유저 존재

        Raises: None
        
        History:
            2020-20-20(홍길동): 초기 생성
            2020-20-21(홍길동): 1차 수정
            2020-20-22(홍길동): 2차 수정
        """

        sql = """
            SELECT * 
            FROM users
            WHERE name = %s;
        """

        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql, username)
            result = cursor.fetchall()
            return result

    def post_dao(self, connection, name, gender, age):
        context = dict()
        context['name'] = name
        context['gender'] = gender
        context['age'] = age
        """유저 정보 생성

        Args:
            connection: 데이터베이스 연결 객체
            name      : 생성할 user 의 name
            gender    : 생성할 user 의 gender
            age       : 생성할 user 의 age

        Author: 홍길동

        Returns:
            return (): 생성 성공

        Raises:
            400, {'message': 'unable to create', 'errorMessage': 'unable_to_create'} : 유저 생성 실패

        History:
            2020-20-20(홍길동): 초기 생성
            2020-20-21(홍길동): 1차 수정
            2020-20-22(홍길동): 2차 수정
        """
        sql = """
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

        with connection.cursor() as cursor:
            cursor.execute(sql, (
                context
            ))
            result = cursor.lastrowid
            if not result:
                raise UserCreateDenied
            return result

    def patch_dao(self, connection, user_id, age):
        context = dict()
        context['user_id'] = user_id
        context['age'] = age

        """유저 정보 수정

        Args:
            connection: 데이터베이스 연결 객체
            user_id   : 수정할 user 의 id
            age       : 수정할 user 의 age

        Author: 홍길동

        Returns: None

        Raises:
            400, {'message': 'unable to update', 'errorMessage': 'unable_to_update'} : 유저 수정 실패
  
        History:
            2020-20-20(홍길동): 초기 생성
            2020-20-21(홍길동): 1차 수정
            2020-20-22(홍길동): 2차 수정
        """

        sql = """
        UPDATE users 
        SET age =%(age)s 
        WHERE id=%(user_id)s;
        """

        with connection.cursor() as cursor:
            affected_row = cursor.execute(sql, (
                context
            ))
            if affected_row == 0:
                raise UserUpdateDenied
