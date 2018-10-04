from api.models.database import Database
from api.user_helper_scripts import format_user_list
db_name = 'fast_food_fast_testing'
class User(object):
    id = 0
    email = ''
    full_name = '' 
    #def __init__(self):
    #    self.id = id 
    #    self.email = email
    #    self.full_name = full_name

    def set_id(self,id):
        self.id = id
    
    def set_email(self,email):
        self.id = email
    
    def set_full_name(self,full_name):
        self.full_name = full_name

    def get_user_data_using_id(self,id):
        db = Database(db_name)
        conn = db.connect_datab()
        cur = conn.cursor()
        cur.execute("SELECT * from users where user_id = '%s'" % (id))
        tup = cur.fetchone()
        user_dict = format_user_list(tup)
        return user_dict

    def validate_admin(self,user):
        if user['admin']==True:
            return True
        else:
            return False
    
    #def check_if_admin(self,id):
