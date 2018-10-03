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

    def save_into_db(self):
        '''
        Save into Database
        '''
        db = Database(self.db_name)
        conn = db.connect_datab()
        cur = conn.cursor()
        cur.execute("INSERT INTO fast_order (user_id,meal_id,order_status) VALUES (%s,%s,'%s')" % (self.order['user_id'],self.order['meal_id'],self.order['status']))
        conn.commit()
        conn.close()

    def validate_status(self,status):
            if status in self.order_statuses:
                return True
            else:
                return False

    def get_order_dic(self):
        return self.order