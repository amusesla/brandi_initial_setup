from flask import jsonify, request
from flask.views import MethodView
from connection import get_connection


class TestUserView(MethodView):
    """데이터베이스 연결을 체크하기 위한 목적으로 제작된 클래스

    Attributes:
        database: app.config['DB']에 담겨있 정보: 데이터베이스 관련 정보
        service: 서비스 클래스 정보

    Author: 홍길동

    History:
        2020-20-20(홍길동): 초기 생성
        2020-20-21(홍길동): 1차 수정
        2020-20-22(홍길동): 2차 수정
    """

    def __init__(self, service, database):
        self.service = service
        self.database = database

    def get(self):
        """        GET 메소드: 해당 유저의 정보를 조회.
        user_id 에 해당되는 유저를 테이블에서 조회 후 가져온다.

        Args:

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

        try:
            connection = get_connection(self.database)
            data = request.json
            user = self.service.get_test_user_service(connection, data)
            return jsonify(user), 200

        finally:
            connection.close()

    def post(self):
        """
        POST 메소드: 유저생성
        Args:

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
        try:
            connection = get_connection(self.database)
            data = request.json
            self.service.post_test_user_service(connection, data)

        except Exception as e:
            connection.rollback()
            return {'status': 400, 'errorMessage': format(e)}

# 클래스를 통해서 response 를 만들자
# 핸들러에서 메세지를 다뤄주면서 message 모양을 만들자
        #make_response

        else:
            connection.commit()
            return {'status': 200, 'message': 'success'}

        finally:
            connection.close()

    def patch(self):
        """
        PATCH 메소드: 유저 정보 수정
        Args:

        Author: 홍길동

        Returns:
            200, { 해당 유저 정보 } : 조회 성공
            400, {'errorMessage': 'unable_to_update'} : 유저 정보 수정 실패

        Raises:

        History:
            2020-20-20(홍길동): 초기 생성
            2020-20-21(홍길동): 1차 수정
            2020-20-22(홍길동): 2차 수정
        """
        try:
            connection = get_connection(self.database)
            data = request.json
            self.service.patch_test_user_service(connection, data)

        except Exception as e:
            connection.rollback()
            return {'status': 400, 'message': format(e)}

        else:
            connection.commit()
            return {'status': 200, 'message': 'success'}

        finally:
            connection.close()

