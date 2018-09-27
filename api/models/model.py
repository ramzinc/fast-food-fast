import json
from api.http_helper_scripts import validate
class Orders(object):
    def  __init__ (self,id,meal_name,price,status):
        self.id = id
        self.meal_name = meal_name
        self.price = price
        self.status = status
    
    def get_order_json(self):
        return json.dumps({'id':self.id,'meal_name':self.meal_name,'price':self.price,'status':self.status})

    