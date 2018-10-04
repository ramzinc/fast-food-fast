from psycopg2 import connect
import os
import flask
#from api.controllers import viewhandle

class Database(object):
    
    
    def __init__(self,db_name):
        self.db_name = db_name
        #flask.g._database =  self.connect_datab()
        run = 0          

    
    def connect_datab(self):
        with connect(dbname=self.db_name, user="postgres") as current_connection:
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
        cursor.execute("DROP TABLE Users ;")
        cursor.execute("DROP TABLE Fast_Order cascade;")
        cursor.execute("DROP TABLE Fast_Meals cascade;")
        conn.commit()
        conn.close()
    def drop_type(self):
        conn = self.connect_datab()
        cursor = conn.cursor()
        cursor.execute("DROP TYPE IF EXISTS status")