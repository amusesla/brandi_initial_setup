""" 엔드 포인트의 시작 및 URL 관리

create_endpoints 함수가 정의되어 있는 곳. 함수 안에 사용할 url endpoint 를 정의한다.
파일 끝에 error_handle()함수를 호출 한다.

기본적인 사용 예시:
    app.add_url_rule('/test', view_func=TestUserView.as_view('test_user_view', test_user_service, database))

"""


from .sample_user_view import SampleUserView
from utils.error_handler import error_handle


def create_endpoints(app, services, database):
    sample_user_service = services.sample_user_service
    """ 앤드 포인트 시작

            Args: 
                app     : Flask 앱
                services: Services 클래스:Service 클래스들을 담고 있는 클래스이다.
                database: 데이터베이스 

            Author: 홍길동

            Returns: None

            Raises: None
            
            History:
                2020-20-20(홍길동): 초기 생성
                2020-20-21(홍길동): 1차 수정
                2020-20-22(홍길동): 2차 수정
            """

# ----------------------------------------------------------------------------------------------------------------------
# Service Section(write your code under your name)
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# 김기용 example ◟( ˘ ³˘)◞ ♡
# ----------------------------------------------------------------------------------------------------------------------
    app.add_url_rule('/test', view_func=SampleUserView.as_view('sample_user_view', sample_user_service, database))

# ----------------------------------------------------------------------------------------------------------------------
# 김민구 ◟( ˘ ³˘)◞ ♡
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Admin 1 Section
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# 이영주 ◟( ˘ ³˘)◞ ♡
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Admin 2 Section
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# 이성보 ◟( ˘ ³˘)◞ ♡
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
    # don't touch this
    error_handle(app)
# ----------------------------------------------------------------------------------------------------------------------
