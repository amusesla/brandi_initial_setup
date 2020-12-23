# custom exception goes here
class UserAlreadyExist(Exception):

    def __init__(self, status_code=400):
        self.status_code = status_code
