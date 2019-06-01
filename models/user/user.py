'''
    author: Zitian(Daniel) Tong
    date: 16:24 2019-05-25 2019
    editor: PyCharm    
    email: danieltongubc@gmail.com 
'''

import uuid
from typing import Dict
from dataclasses import dataclass, field
from Pricing_Service.models.model import Model
from Pricing_Service.common.utils import Utils
import Pricing_Service.models.user.errors as UserErrors


@dataclass
class User(Model):
    collection: str = field(init=False, default="users")
    email: str
    password: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    @classmethod
    def find_by_email(cls, email: str) -> "User":
        try:
            return cls.find_one_by('email', email)
        except TypeError:
            raise UserErrors.UserNotFoundError('A user with this email was not found')

    @classmethod
    def is_login_valid(cls, email: str, password: str) -> bool:
        user = cls.find_by_email(email)

        if not Utils.check_hashed_password(password, user.password):
            raise UserErrors.IncorrectPasswordError('Your password is incorrect')

        return True

    @classmethod
    def register_user(cls, email: str, password: str) -> bool:
        '''
        This method register a user using email and password
        :param email: user's email
        :param password: user's password
        :return: True if register successfully, False otherwise
        '''

        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError('The email does not have the right format')

        try:
            user = User.find_by_email(email)
            raise UserErrors.UserAlreadyRegisteredError('The email you used to register already exists.')
        except UserErrors.UserNotFoundError:
            User(email, Utils.hash_password(password)).save_to_mongo()

        return True

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
        }


