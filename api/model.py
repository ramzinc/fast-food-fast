import json

class Orders(object):

    def  __init__ (self,id,meal_name,price,status):
        self.id = id
        self.meal_name = meal_name
        self.price = price
        self.status = status
        #self.list_order = list()
    def get_order_json(self):
        ord = {'id':self.id,'meal_name':self.meal_name,'price':self.price,'status':self.status}
        #self.list_order.append(ord)
        #return json.dumps(ord)
        return ord
    
