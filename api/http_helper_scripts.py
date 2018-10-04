
from api.models.model import Meals
from api.models.database import Database
from flask import jsonify,make_response
#orders = [{'id': 1,'meal_name':'matooke' ,'price':4000},{'id':2,'meal_name':'chickentika','price':6000,'status': False},
#                   {'id': 3,'meal_name': 'beans' ,'price':1000, 'status': False}]

#validate if there no id , and a string of meal_name and price is an int
db_name ="fast_food_fast_testing"
def validate_food(order):
    #for i in order:
    if 'id' not in order and 'meal_name' in order and 'price' in order and isinstance(order['price'],int):
        #import pdb;pdb.set_trace()
        return True
    else:
        #import pdb;pdb.set_trace()
        return False

def check_id_present(order_id):
        db = Database(db_name)
        conn = db.connect_datab()
        cur = conn.cursor()
        cur.execute("SELECT order_id from fast_order;")
        order_idz = cur.fetchall()
        for i in order_idz:
            if order_id in i:
                return True
            else:
                continue
        return False

            

    
def change_status(order_status,order_id):
        db = Database(db_name)
        conn = db.connect_datab()
        cur = conn.cursor()
        cur.execute("UPDATE fast_order SET order_status = '%s' where order_id=%s;" % (order_status,order_id))
        conn.commit()
        conn.close()
        return make_response(jsonify({"Changed order with id %s" % (order_id):order_status }))

        

def insert_data(ps_order,current_list):
    #id =  int(id)
   # order = dict()
    #id = id + 1
    current_list.append(Meals(ps_order['meal_name'],ps_order['price']).get_order_json())
    #import pdb; pdb.set_trace()
    insert_meal_data_into_mealtb(current_list)
    #; pdb.set_trace()
    #return current_list      

def insert_meal_data_into_mealtb(current_list):

    
    db = Database(db_name)
    conn = db.connect_datab()
    db.execute_query()
    for i in current_list:
       cur = conn.cursor()
       cur.execute("INSERT INTO Fast_Meals (meal_name,price) VALUES (%s,%s)",(i['meal_name'],i['price'])) 
    conn.commit()
    conn.close()

def check_if_list(lst):
    if isinstance(lst,list):
        return True
    else:
        return False

def get_order(id,order_list):
    for i in order_list:
        if i["id"] == id:
            return i
        continue

def validate_status(req_status):
    status = ('New','Processing','Cancelled','Complete')
    if req_status['status'] in status:
        return True
    else:
        return False