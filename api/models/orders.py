from api.models.database import Database
from flask import jsonify 
import json
from api.user_helper_scripts import get_meal_id
class Orders(object):
    db_name = "fast_food_fast_testing"    
    order ={}
    status =''
    order_statuses = ('New','Processing','Cancelled','Complete')
    def __init__(self,meal_name,current_user):
        self.meal_name = meal_name
        self.user_id = current_user # Incase I have to use the value somewhere
        self.order['user_id']= self.user_id

    def get_quantity(self):
        db = Database(self.db_name)
        conn = db.connect_datab()
        cur = conn.cursor()
        cur.execute("SELECT quantity from fast_order where user_id = %s and meal_id = %s;" % (self.order['user_id'],self.order['meal_id']))
        tup_returned  = cur.fetchone()
        import pdb;pdb.set_trace()
        #return tup_returned
        if not tup_returned == None:
                self.order['quantity'] = tup_returned[0]+1
                #self.save_quantity_alone()
                return self.order['quantity']
        else:
                self.order['quantity'] = 1
                return self.order['quantity']
        conn.close()
        
    def set_meal_id(self):
        meal_id = get_meal_id(self.db_name,self.meal_name)
        #import pdb;pdb.set_trace()
        self.order['meal_id'] = meal_id

    def set_status(self,status):
        if self.validate_status(status):
            self.status  = status
            self.order['status']= status
        else:
            return jsonify({'Error':"The Status You Have Entered Is Wrong"})

    def save_quantity_alone(self):
        db = Database(self.db_name)
        conn = db.connect_datab()
        cur = conn.cursor()
        cur.execute("SELECT order_id FROM fast_order WHERE user_id = %s and meal_id = %s;" % (self.order['user_id'],self.order['meal_id']))
        order_id_tp= cur.fetchone()
        order_id = order_id_tp[0]
        cur.execute("UPDATE fast_order SET quantity = (%s) where order_id = %s ;" % (self.order['quantity'],order_id))
        conn.commit()
        conn.close()
        return "Print Valid"

    def get_order_id(self):
        db = Database(self.db_name)
        conn = db.connect_datab()
        cur = conn.cursor()
        order_id = cur.execute("SELECT order_id FROM fast_order WHERE user_id = %s and meal_id = %s;" % (self.order['user_id'],self.order['meal_id']))
        return order_id

    def save_into_db(self):
        '''
        Save into Database
        '''
        db = Database(self.db_name)
        conn = db.connect_datab()
        cur = conn.cursor()
        cur.execute("INSERT INTO fast_order (user_id,meal_id,order_status,quantity) VALUES (%s,%s,'%s',%s);" % (self.order['user_id'],self.order['meal_id'],self.order['status'],self.order['quantity']))
        conn.commit()
        conn.close()

   #
   #   
   # 
   #
   #    
   #   
   #

    def validate_status(self,status):
            if status in self.order_statuses:
                return True
            else:
                return False

    #This gets the id from the orders table 
    def get_meal_id_from_user_id(self,user_id):
        db = Database(self.db_name)
        conn = db.connect_datab()
        cur = conn.cursor()
        cur.execute("SELECT meal_id,quantity from fast_order where user_id= '%s';" % (user_id))
        meal_id_tup = cur.fetchall()
        
                

    def get_meal_name_from_id(self,meal_id):
        meal_name_dict = dict()
        db = Database(self.db_name)
        conn = db.connect_datab()
        cur = conn.cursor()
        cur.execute("SELECT meal_name from fast_meals where meal_id = '%s'" %(meal_id))
        meal_name_tup = cur.fetchone()
        meal_name_dict['meal_name'] = meal_name_tup[0]
        return meal_name_dict
        



    def get_order_dic(self):
        return self.order