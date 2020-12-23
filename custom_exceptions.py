# custom exception goes here
class UserAlreadyExist(Exception):
    pass


class UserUpdateDenied(Exception):
    pass


class UserCreateDenied(Exception):
    pass


class UserNotExist(Exception):
    pass
