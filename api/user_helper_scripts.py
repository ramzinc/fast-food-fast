from api.models.database import Database
import json
db_name = 'fast_food_fast_testing'
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
    db = Database(db_name)
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
    db = Database(db_name)
    db.execute_query()
    conn = db.connect_datab()
    cur = conn.cursor()
    cur.execute("SELECT * from fast_meals;")
    lis = cur.fetchall()
    conn.close()
    #ret_d = format_menu_list(lis)
    return lis

#def format_menu_list(lis):
#    ret_dic = dict()
#    for i in lis:
#        ret_dic['id'],ret_dic['meal_name'],ret_dic['price']= i[0],i[1],i[2]
#        
#    return ret_dic
        
def get_user_data(req_data):
    '''
    Return a tuple of data that matches the user details
    '''
    db = Database(db_name)
    conn = db.connect_datab()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Users where email = %s and password = %s;",(req_data['email'],req_data['password']))
    ret_tup = cur.fetchone()
    conn.close()
    #import pdb; pdb.set_trace()
    ret_dic =format_user_list(ret_tup)
    return ret_dic

def format_user_list(ret_tup):
    new_dic = dict()
    #import pdb;pdb.set_trace()
    new_dic['id'],new_dic['full_name'],new_dic['admin'],new_dic['email'],new_dic['password'] = ret_tup
    return new_dic

def validate_signin_data(req_data):
    if 'password' in req_data and 'email' in req_data:
        return True
    else:
        return False

def get_meal_id(db_in,meal_name):
        #query = 'SELECT id From fast_meals WHERE fastmeals.meal_name = %s;',(meal_name)
        db = Database(db_in)
        db.execute_query()   #incase post order is None
        conn = db.connect_datab()
        cur = conn.cursor()
        cur.execute("SELECT meal_id from fast_meals WHERE meal_name = '%s';" % (meal_name))
        meal_id = cur.fetchone()
        return meal_id[0]
    
def get_orders():
    
    db = Database(db_name)
    conn =  db.connect_datab()
    cur = conn.cursor()
    cur.execute("SELECT * FROM fast_order;")
    ord_tup = cur.fetchall()
    #ret_order = json.dumps(ord_tup)
    return ord_tup

def format_order_ret(ord_tup):
    ret_dic = dict()
    ret_list = list()
    import pdb;pdb.set_trace()
    for i in ord_tup:
        import pdb;pdb.set_trace()
        ret_dic['order_id'],ret_dic['user_id'],ret_dic['meal_id'],ret_dic['order_status'],ret_dic['quantity'] = i
        import pdb;pdb.set_trace()
        ret_list.append(ret_dic)
    return ret_list