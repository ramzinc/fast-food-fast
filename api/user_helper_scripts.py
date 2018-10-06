from api.models.database import Database
from flask import jsonify,make_response
#from api.http_helper_scripts import get_db_name
db_name = 'fast_food_fast_testing'
#db_name = get_db_name()
from api.models.users import User
def validate_user(req_data):
    if 'first_name' in req_data and isinstance(req_data['first_name'],str) and isinstance(req_data['last_name'],str) and is_email(req_data['email']):
        return True
    else:
        return False
def is_email(email_to):
    if '@' in email_to:
        return True
    else:
        return False

def is_admin(req_data):
    '''
    Check wether the user is signed up as admin
    '''
    if 'admin' in req_data and req_data['admin'] == True :
        return True
    else:
        return False

def insert_user_data_into_userdb(user_data):
    '''
    Insert user data into the users table in the database
    '''
    full_name = user_data['first_name'] + ' ' + user_data['last_name']
    db = Database()
    if is_admin(user_data):
        admin = True 
    else:
        admin = False
    conn = db.connect_datab()
    db.execute_query()
    #for i in user_data:
    cur = conn.cursor()
    cur.execute("INSERT INTO Users (full_name,admin,email,password) VALUES (%s,%s,%s,%s)",(full_name,admin,user_data['email'],user_data['password']))
    conn.commit()
    conn.close()

def get_menu_items():
    #ret_d = dict()
    db = Database()
    db.execute_query()
    conn = db.connect_datab()
    cur = conn.cursor()
    cur.execute("SELECT * from fast_meals;")
    lis = cur.fetchall()
    conn.close()
    ret_d = format_menu_list(lis)
    return ret_d

def format_menu_list(lis):
    
    ret_list = list()
    for i in lis:
        ret_dic = dict()
        #import pdb;pdb.set_trace()
        ret_dic['id'],ret_dic['meal_name'],ret_dic['price']= i
        #import pdb;pdb.set_trace()
        ret_list.append(ret_dic)
        #import pdb;pdb.set_trace
        #continue
    #import pdb;pdb.set_trace()
    return ret_list
        
def get_user_data(req_data):
    '''
    Return a tuple of data that matches the user details
    '''
    db = Database()
    conn = db.connect_datab()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Users where email = %s and password = %s;",(req_data['email'],req_data['password']))
    ret_tup = cur.fetchone()
    conn.close()
    usr = User()
    #import pdb; pdb.set_trace()
    ret_dic = usr.format_user_list(ret_tup)
    return ret_dic

def validate_signin_data(req_data):
    if 'password' in req_data and 'email' in req_data:
        return True
    else:
        return False

def get_meal_id(meal_name):
    #query = 'SELECT id From fast_meals WHERE fastmeals.meal_name = %s;',(meal_name)
    db = Database()
    db.execute_query()   #incase post order is None
    conn = db.connect_datab()
    cur = conn.cursor()
    cur.execute("SELECT meal_id from fast_meals WHERE meal_name = '%s';" % (meal_name))
    meal_id = cur.fetchone()
    return meal_id[0]
    
def get_orders():
    
    db = Database()
    conn =  db.connect_datab()
    cur = conn.cursor()
    cur.execute("SELECT * FROM fast_order;")
    ord_tup = cur.fetchall()
    ret_order = format_order_ret(ord_tup)
    return ret_order

def format_order_ret(ord_tup):
    ret_list = list()
    usr = User()
    #import pdb;pdb.set_trace()
    for i in ord_tup:
        ret_dic_id = dict()
        ret_dic_data = dict()
        #import pdb;pdb.set_trace()
        ret_dic_id['order_id'],ret_dic_id['user_id'],ret_dic_id['meal_id'],ret_dic_id['order_status'],ret_dic_id['quantity'] = i
        ret_dic_data['user_name'] = usr.get_user_data_using_id(ret_dic_id['user_id'])['full_name']
        #import pdb;pdb.set_trace()
        ret_dic_data['meal_name'] = usr.get_meal_name_from_id(ret_dic_id['meal_id'])
        #import pdb;pdb.set_trace()
        ret_dic_data['order_status'] = ret_dic_id['order_status']
        # pdb;pdb.set_trace()
        ret_dic_data['quantity'] = ret_dic_id['quantity']        
        #import pdb;pdb.set_trace()
        ret_list.append(ret_dic_data)
        #import pdb;pdb.set_trace()
        continue
        #import pdb;pdb.set_trace()
    return ret_list

def get_specific_order(order_id):
    db = Database()
    conn =  db.connect_datab()
    cur = conn.cursor()
    cur.execute("SELECT meal_id FROM fast_order where order_id = %s;" % (order_id))
    ord_tup = cur.fetchone()
    meal_id = ord_tup[0]
    cur.execute("SELECT meal_name FROM fast_meals WHERE meal_id = %s;" % (meal_id))
    meal_name_tup =  cur.fetchone()
    if meal_name_tup == None:
        return make_response(jsonify({"Error_Msg": "No such Order"}))
    meal_name = meal_name_tup[0]
    return meal_name