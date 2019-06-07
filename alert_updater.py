'''
    author: Zitian(Daniel) Tong
    date: 14:24 2019-05-05 2019
    editor: PyCharm    
    email: danieltongubc@gmail.com 
'''

from models.alert import Alert

alerts = Alert.all()

for alert in alerts:
    alert.load_item_price()
    print(alert.load_item_price())
    print(alert.price_limit)
    alert.notify_if_price_reached()


if not alerts:
    print("No alers have been created. Add an item and an Alert to begin !")

