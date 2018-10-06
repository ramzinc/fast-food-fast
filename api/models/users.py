from api.models.database import Database
#from api.models.orders import Orders
from flask import jsonify,make_response
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
        db = Database()
        db.execute_query()
        conn = db.connect_datab()
        cur = conn.cursor()
        cur.execute("SELECT * from users where user_id = '%s'" % (id))
        tup = cur.fetchone()
        user_dict = self.format_user_list(tup)
        return user_dict
    

    def format_user_list(self,ret_tup):
         new_dic = dict()
         #import pdb;pdb.set_trace()
         new_dic['id'],new_dic['full_name'],new_dic['admin'],new_dic['email'],new_dic['password'] = ret_tup
         return new_dic

    def get_all_user_ids(self):
        db = Database()
        db.execute_query()
        conn = db.connect_datab()
        cur = conn.cursor()
        cur.execute("SELECT user_id from users;")
        tup = cur.fetchall()
        #import pdb;pdb.set_trace()
        return tup
    
    def check_if_user_id_indb(self,user_id):
        #import pdb;pdb.set_trace()
        tup = self.get_all_user_ids()
        for i in tup:
            #import pdb;pdb.set_trace()
            if user_id  in i:
                return True
            else:
                #import pdb;pdb.set_trace()
                continue
        return False
                
       

    def validate_admin(self,user):
        '''
        Check if user is an admin or not
        '''
        if user['admin']==True:
            return True
        else:
            return False
    
    def validate_request(self,req_data):
        if 'user_id' in req_data:
            return True
        else:
            return False

    def check_for_specific_usr_ord(self,user_id):
        '''
        Checks for the users specific Order
        '''
        #import pdb;pdb.set_trace()
        user_ord_tuple = self.get_meal_id_from_user_id(user_id)

        meal_ord_dict = {}
        meal_names = []
        #import pdb;pdb.set_trace()
        for i in user_ord_tuple:
            meal_ord_dict['id'],meal_ord_dict['quantity'] = i
            #import pdb;pdb.set_trace()
            meal_names.append(self.get_meal_name_from_id(meal_ord_dict['id']))
            #order_meal.append(meal_ord_dict)
            #import pdb;pdb.set_trace()

        return meal_names


    def get_meal_id_from_user_id(self,user_id):
        '''
        This gets the meal_id from the orders table using The user_id
        '''
        #import pdb;pdb.set_trace()
        db = Database()
        conn = db.connect_datab()
        cur = conn.cursor()
        cur.execute("SELECT meal_id,quantity from fast_order where user_id=%s;" % (user_id))
        meal_id_tup = cur.fetchall()
        #import pdb;pdb.set_trace()
        return meal_id_tup



    def get_meal_name_from_id(self,meal_id):
        '''
        Gets meal_name From meal_id 
        '''
        meal_name_dict = dict()
        db = Database()
        conn = db.connect_datab()
        cur = conn.cursor()

        cur.execute("SELECT meal_name from fast_meals where meal_id = '%s'" %(meal_id))
        meal_name_tup = cur.fetchone()
        meal_name_dict['meal_name'] = meal_name_tup[0]
        #import pdb;pdb.set_trace()
        return meal_name_dict
    
    def check_if_user_exists(self,user_info):
        '''
        check if user is in db
        '''
        if self.check_email_in_db(user_info):
            #import pdb;pdb.set_trace()
            return '' 
        else:
            #import pdb;pdb.set_trace()
            return True

    
    def check_email_in_db(self,user_info):
        all_users = self.get_all_user_info()
        for i in all_users:
            if user_info['email'] in i:
                #import pdb;pdb.set_trace()
                return True
            else:

                #import pdb;pdb.set_trace()
                continue
        return False


    def get_all_user_info(self):
        db = Database()
        db.execute_query()
        conn = db.connect_datab()
        cur = conn.cursor()
        cur.execute("SELECT * from users;")
        all_users = cur.fetchall()
        #import pdb;pdb.set_trace()
        return all_users
