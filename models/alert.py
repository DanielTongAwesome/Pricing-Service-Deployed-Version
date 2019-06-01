'''
    author: Zitian(Daniel) Tong
    date: 13:57 2019-05-05 2019
    editor: PyCharm    
    email: danieltongubc@gmail.com 
'''


import uuid
from typing import Dict
from dataclasses import dataclass, field
from Pricing_Service.models.item import Item
from Pricing_Service.models.model import Model
from Pricing_Service.models.user.user import User


@dataclass(eq=False)    # no need to compare two alerts
class Alert(Model):

    collection: str = field(init=False, default='alerts')   # since init is false so it cannot be modified
    name: str
    item_id: str
    price_limit: float
    user_email: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def __post_init__(self):
        # dataclass will auto generate this
        # super().__init__()
        self.item = Item.find_by_id(self.item_id)
        self.user = User.find_by_email(self.user_email)

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "name": self.name,
            "price_limit": self.price_limit,
            "item_id": self.item_id,
            'user_email': self.user_email
        }

    def load_item_price(self) -> float:
        self.item.load_price()
        return self.item.price

    def notify_if_price_reached(self):
        if self.item.price < self.price_limit:
            print('Item {} has reached a price under {}. Latest Price: {}'.format(self.item, self.price_limit, self.item.price))



