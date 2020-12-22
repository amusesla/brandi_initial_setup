class TestUserService:
    def __init__(self, test_user_dao):
        self.test_user_dao = test_user_dao

    def get_test_user_service(self, connection, data):

        """
        해당 아이디를 가진 유저를 검색 함수
        Args:
            connection: 데이터베이스 연결 객체
            data      : front 에서 넘겨받은 json 객체

        Author: 홍길동

        Returns:
            200, { 해당 유저 정보 } : 조회 성공

        History:
            2020-20-20(홍길동): 초기 생성
            2020-20-21(홍길동): 1차 수정
            2020-20-22(홍길동): 2차 수정

        Raises:
        """

        user_id = data['user_id']
        return self.test_user_dao.get_dao(connection, user_id)

    def post_test_user_service(self, connection, data):
        """
        POST 메소드: 유저생성

        Args:
            connection: 데이터베이스 연결 객체
            data      : front 에서 넘겨받은 json 객체

        Author: 홍길동

        Returns:
            200, { 해당 유저 정보 } : 조회 성공

        History:
            2020-20-20(홍길동): 초기 생성
            2020-20-21(홍길동): 1차 수정
            2020-20-22(홍길동): 2차 수정

        Raises:
        """
        name = data['name']
        gender = data['gender']
        age = data['age']
        return self.test_user_dao.post_dao(connection, name, gender, age)

    def patch_test_user_service(self, connection, data):
        """
        PATCH 메소드: 유저 정보 수정

        Args:
            connection: 데이터베이스 연결 객체
            data      : front 에서 넘겨받은 json 객체

        Author: 홍길동

        Returns:
            200, { 해당 유저 정보 } : 조회 성공

        History:
            2020-20-20(홍길동): 초기 생성
            2020-20-21(홍길동): 1차 수정
            2020-20-22(홍길동): 2차 수정

        Raises:
        """
        user_id = data['user_id']
        age = data['age']
        return self.test_user_dao.patch_dao(connection, user_id, age)