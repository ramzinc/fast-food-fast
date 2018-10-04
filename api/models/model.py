import json

class Meals(object):
    
    ord = {}
    def  __init__ (self,meal_name,price):
        #self.id = id
        self.meal_name = meal_name
        self.price = price
        #self.status = status
        #self.list_order = list()
    def get_order_json(self):
        ord = {'meal_name':self.meal_name,'price':self.price}
        #self.list_order.append(ord)
        #return json.dumps(ord)
        return ord
    
