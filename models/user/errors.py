'''
    author: Zitian(Daniel) Tong
    date: 16:24 2019-05-25 2019
    editor: PyCharm    
    email: danieltongubc@gmail.com 
'''


class UserError(Exception):
    def __init__(self, message):
        self.message = message


class UserNotFoundError(UserError):
    pass


class UserAlreadyRegisteredError(UserError):
    pass


class InvalidEmailError(UserError):
    pass


class IncorrectPasswordError(UserError):
    pass

