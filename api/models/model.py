import json
from api.models.database import Database

class Meals(object):
    db_name = 'fast_food_fast_testing'    
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
    
    def get_meal_from_id(self,meal_id):
        db = Database(self.db_name)
        conn = db.connect_datab()
        cur = conn.cursor()
        cur.execute("SELECT * from fast_meals where meal_id = %s;" % (meal_id))
        meal_name_tup = cur.fetchone()
        meal_name = meal_name_tup[0]
        return meal_name