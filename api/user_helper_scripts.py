from api.models.database import Database
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
    if 'admin' in req_data and req_data['admin'] == True :
        return True
    else:
        return False

def insert_user_data_into_userdb(user_data):
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
