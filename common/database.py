'''
    author: Zitian(Daniel) Tong
    date: 02:07 2019-05-05 2019
    editor: PyCharm    
    email: danieltongubc@gmail.com 
'''

import pymongo
from typing import Dict


class Database(object):
    URI = "mongodb://127.0.0.1:27017/pricing_service"
    DATABASE = pymongo.MongoClient(URI).get_database()

    @staticmethod
    def insert(collection: str, data: Dict):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query) -> Dict:
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].remove(query)

