"""사용자 제작 예외 처리

앱 관련 사용자 제작 예외처리는 모두 이곳에 Exception 클래스를 상속받아 작성한다.
작성한 사용제 제작 예외 처리는 error_handler.py 에서 사용된다.

기본적인 사용 예시:
  class IamException(Exception):
    pass

"""


class UserAlreadyExist(Exception):
    pass


class UserUpdateDenied(Exception):
    pass


class UserCreateDenied(Exception):
    pass


class UserNotExist(Exception):
    pass


class DatabaseCloseFail(Exception):
    pass
