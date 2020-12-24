from flask import jsonify
from flask.views import MethodView
from connection import get_connection
from custom_exceptions import DatabaseCloseFail
from flask_request_validator import (
    Param,
    JSON,
    validate_params
)


class TestUserView(MethodView):
    """ Presentation Layer

    Attributes:
        database: app.config['DB']에 담겨있는 정보(데이터베이스 관련 정보)
        service : TestUserService 클래스

    Author: 홍길동

    History:
        2020-20-20(홍길동): 초기 생성
        2020-20-21(홍길동): 1차 수정
        2020-20-22(홍길동): 2차 수정
    """

    def __init__(self, service, database):
        self.service = service
        self.database = database

    @validate_params(
        Param('user_id', JSON, int, rules=[])
    )
    def get(self, *args):

        data = {
            'user_id': args[0]
        }
        """GET 메소드: 해당 유저의 정보를 조회.

        user_id 에 해당되는 유저를 테이블에서 조회 후 가져온다.

        Args: None

        Author: 홍길동

        Returns:
            return {"message": "success", "result": [{"age": "18", "gender": "남자", "id": 12, "name": "김민구12"}]}

        Raises:
            400, {'message': 'key error', 'errorMessage': 'key_error'}                              : 잘못 입력된 키값
            400, {'message': 'user does not exist error', 'errorMessage': 'user_does_not_exist'}    : 유저 정보 조회 실패
            400, {'message': 'unable to close database', 'errorMessage': 'unable_to_close_database'}: 커넥션 종료 실패
            500, {'message': 'internal server error', 'errorMessage': format(e)})                   : 서버 에러

        History:
            2020-20-20(홍길동): 초기 생성
            2020-20-21(홍길동): 1차 수정
            2020-20-22(홍길동): 2차 수정
        """

        try:
            connection = get_connection(self.database)
            user = self.service.get_test_user_service(connection, data)
            return jsonify({'message': 'success', 'result': user})

        except Exception as e:
            raise e
        finally:
            try:
                if connection:
                    connection.close()
            except DatabaseCloseFail:
                raise DatabaseCloseFail

    @validate_params(
        Param('name', JSON, str),
        Param('gender', JSON, str),
        Param('age', JSON, int)
    )
    def post(self, *args):
        data = {
            'name': args[0],
            'gender': args[1],
            'age': args[2]
        }
        """POST 메소드: 유저생성

        Args: None

        Author: 홍길동

        Returns:
            200, {'message': 'success'}                                                             : 유저 생성 성공

        Raises:
            400, {'message': 'key error', 'errorMessage': 'key_error'}                              : 잘못 입력된 키값
            400, {'message': 'user create error', 'errorMessage': 'user_create_error'}              : 유저 생성 실패
            403, {'message': 'user already exist', errorMessage': 'already_exist'}                  : 중복 유저 생성 실패
            400, {'message': 'unable to close database', 'errorMessage': 'unable_to_close_database'}: 커넥션 종료 실패
            500, {'message': 'internal server error', 'errorMessage': format(e)})                   : 서버 에러

        History:
            2020-20-20(홍길동): 초기 생성
            2020-20-21(홍길동): 1차 수정
            2020-20-22(홍길동): 2차 수정
        """

        try:

            connection = get_connection(self.database)
            self.service.post_test_user_service(connection, data)
            connection.commit()
            return {'message': 'success'}

        except Exception as e:
            connection.rollback()
            raise e

        finally:
            try:
                if connection:
                    connection.close()
            except DatabaseCloseFail:
                raise DatabaseCloseFail

    @validate_params(
        Param('user_id', JSON, int),
        Param('age', JSON, int)
    )
    def patch(self, *args):
        data = {
            'user_id': args[0],
            'age': args[1]
        }

        """PATCH 메소드: 유저 정보 수정

        Args: None

        Author: 홍길동

        Returns:
            200, {'message': 'success'}                                                             : 유저 생성 성공

        Raises:
            400, {'message': 'key error', 'errorMessage': 'key_error'}                              : 잘못 입력된 키값
            400, {'message': 'unable to update', 'errorMessage': 'unable_to_update'}                : 유저 정보 수정 실패
            400, {'message': 'unable to close database', 'errorMessage': 'unable_to_close_database'}: 커넥션 종료 실패
            500, {'message': 'internal server error', 'errorMessage': format(e)})                   : 서버 에러

        History:
            2020-20-20(홍길동): 초기 생성
            2020-20-21(홍길동): 1차 수정
            2020-20-22(홍길동): 2차 수정
        """

        try:
            connection = get_connection(self.database)
            self.service.patch_test_user_service(connection, data)
            connection.commit()
            return {'message': 'success'}

        except Exception as e:
            connection.rollback()
            raise e

        finally:
            try:
                if connection:
                    connection.close()
            except DatabaseCloseFail:
                raise DatabaseCloseFail
