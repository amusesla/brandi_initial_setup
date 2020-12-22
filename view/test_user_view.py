from flask import jsonify, request
from flask.views import MethodView
from connection import get_connection

# InterfaceError, 데이터 조작 할 때 컬럼 개수와 value 개수가 불일치.
# DatabaseError, 데이터베이스 시스템 실패.
# DataError, 데이터를 집계 불가.(null 불가 필드에 null 입력, 0으로 나누는 연산 등)
# OperationalError, 너무 많은 데이터베이스 접속, 데이터소스 이름 없음, 트랜젝션 실행불가, 메모리 할당 에러, 연결 끊김 등 에러
# IntegrityError, 유효하지 않은 cursor, foreignkey 검사 실패로 인한 트랜젝션 실패.
# ProgrammingError, SQL 문법에러, 매개변수 수가 불일치,
# NotSupportedError, SQL 버전에 맞지 않는 기능 사용 및 SQL 루틴에 맞지 않는 명령실행(rollback 을 끝난 트랜젝션에 요구)

class TestUserView(MethodView):
    """데이터베이스 연결을 체크하기 위한 목적으로 제작된 클래스

      Attributes:
          database: app.config['DB']에 담겨있 정보: 데이터베이스 관련 정보.
          service: 서비스 클래스 정보.
      """

    def __init__(self, service, database):
        self.service = service
        self.database = database

    def get(self):
        """GET 메소드: 해당 유저의 정보를 조회.
            user_id 에 해당되는 유저를 테이블에서 조회 후 가져온다.

            Args:

            Returns:
                200, { 해당 유저 정보 } : 조회 성공
                400, {'errorMessage': 'user_does_not_exist'} : 유저 정보 조회 실패
            Raises:
        """

        try:
            connection = get_connection(self.database)
            data = request.json
            user = self.service.get_test_user_service(connection, data)
            return jsonify(user), 200

        except Exception as e:
            return {'status': 400, 'errorMessage': format(e)}

        finally:
            connection.close()

    def post(self):
        """POST 메소드: 유저생성
            Args:

            Returns:

                200, { 해당 유저 정보 } : 조회 성공
                400, {'errorMessage': 'user_does_not_exist'} : 유저 정보 조회 실패

            Raises:
        """
        try:
            connection = get_connection(self.database)
            data = request.json
            self.service.post_test_user_service(connection, data)

        except Exception as e:
            connection.rollback()
            return {'status': 400, 'errorMessage': format(e)}

        else:
            connection.commit()
            return {'status': 200, 'message': 'success'}

        finally:
            connection.close()

    def patch(self):
        """PATCH 메소드: 유저 정보 수정
            Args:

            Returns:
                200, { 해당 유저 정보 } : 조회 성공
                400, {'errorMessage': 'unable_to_update'} : 유저 정보 수정 실패

            Raises:
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

