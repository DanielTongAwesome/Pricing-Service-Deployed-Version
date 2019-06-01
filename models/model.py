'''
    author: Zitian(Daniel) Tong
    date: 00:00 2019-05-06 2019
    editor: PyCharm    
    email: danieltongubc@gmail.com 
'''

from typing import List, Dict, TypeVar, Type
from abc import ABCMeta, abstractmethod
from Pricing_Service.common.database import Database

T = TypeVar('T', bound='Model')


class Model(metaclass=ABCMeta):
    collection = 'model_error'    # models are not going to be used, just for getting rid of warning
    _id = '0'

    def __init__(self, *args, **kwargs):  # this are not going to be used, just for getting rid of warning
        pass

    def save_to_mongo(self):
        Database.update(self.collection, {"_id": self._id}, self.json())

    def remove_from_mongo(self):
        Database.remove(self.collection, {"_id": self._id})

    @classmethod
    def find_by_id(cls: Type[T], _id: str) -> T:
        return cls.find_one_by("_id", _id)

    @abstractmethod
    def json(self) -> Dict:
        raise NotImplementedError

    @classmethod
    def all(cls: Type[T]) -> List[T]:
        elements_from_db = Database.find(cls.collection, {})
        return [cls(**element) for element in elements_from_db]

    @classmethod
    def find_one_by(cls: Type[T], attribute: str, value: str) -> T:  # Item.find_one_by{'url' : 'www.bla.com'}
        return cls(**Database.find_one(cls.collection, {attribute: value}))

    @classmethod
    def find_many_by(cls: Type[T], attribute: str, value: str) -> List[T]:  # Item.find_many_by{ 'url' : 'www.bla.com'}
        return [cls(**element) for element in Database.find(cls.collection, {attribute: value})]