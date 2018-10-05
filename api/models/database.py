from psycopg2 import connect
import os
import flask
#from api.controllers import viewhandle
#from api.http_helper_scripts import DbName
class Database(object):


    def __init__(self):
        db_name = DbName()
        self.conn_info = db_name.get_conn_info()
        #flask.g._database =  self.connect_datab()
        #run = 0          

    
    def connect_datab(self):
        with connect(dbname=self.conn_info['db_name'], user=self.conn_info['db_user']) as current_connection:
            return current_connection
    
    def execute_query(self):
        connect = self.connect_datab()
        cursor = connect.cursor()
        #with viewhandle.app.open_resource('schema.sql') as schema:
            #cursor.execute(schema.read())
        cursor.execute("CREATE TABLE IF NOT EXISTS Users(user_id SERIAL primary key ,full_name text ,admin boolean,email text UNIQUE,password text);")
        cursor.execute("CREATE TABLE IF NOT EXISTS Fast_Meals(meal_id SERIAL PRIMARY KEY , meal_name text UNIQUE,price integer);")
        #cursor.execute("CREATE TYPE ord_status AS ENUM ('New','Processing','Cancelled','Complete');")
        cursor.execute("CREATE TABLE IF NOT EXISTS Fast_Order(order_id  SERIAL PRIMARY KEY ,user_id int  REFERENCES Users (user_id) ON UPDATE CASCADE ON DELETE RESTRICT,meal_id int  REFERENCES Fast_Meals (meal_id),order_status text,quantity int);")
        connect.commit()
        connect.close()
        
    def drop_tables(self):
        conn = self.connect_datab()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE Users Cascade ;")
        cursor.execute("DROP TABLE Fast_Order cascade;")
        cursor.execute("DROP TABLE Fast_Meals cascade;")
        conn.commit()
        conn.close()
    def drop_type(self):
        conn = self.connect_datab()
        cursor = conn.cursor()
        cursor.execute("DROP TYPE IF EXISTS status")


class DbName(object):
    def get_conn_info(self):
        conn_info = {}
        environment = os.getenv("Environment")
        if environment == 'Development':
            conn_info['db_user']='postgres' 
            conn_info['db_name']= 'fast_food_fast_testing'
            conn_info['db_host']='localhost'
            conn_info['db_port']='5432' 
            conn_info['db_password']=''
            return conn_info
        else:
            conn_info['db_host']='ec2-23-23-80-20.compute-1.amazonaws.com'
            conn_info['db_name']= 'dfn51nqle2hqlh'
            conn_info['db_user']= 'glqcusjgplusqy'
            conn_info['db_port']= '5432'
            conn_info['db_password']= db_password = '00e3f558f2568f0b7efae7b082a3833eae4be9e10ee27c6865dd082f328e3e18'
            return conn_info
