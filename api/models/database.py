from psycopg2 import connect
import os
import flask
#from api.controllers import viewhandle

class Database(object):
    #db_name = DATABASE_URI= "postgres://postgres@localhost:5432/fast_food_fast_prod"
    def __init__(self,db_name):
        self.db_name = db_name
        #flask.g._database =  self.connect_datab()
                  

    
    def connect_datab(self):
        with connect(dbname=self.db_name, user="postgres") as current_connection:
            return current_connection
    
    def execute_query(self):
        connect = self.connect_datab()
        cursor = connect.cursor()
        #with viewhandle.app.open_resource('schema.sql') as schema:
            #cursor.execute(schema.read())
        cursor.execute("CREATE TABLE IF NOT EXISTS Users(user_id SERIAL primary key ,full_name text ,admin boolean,email text,password text);")
        cursor.execute("CREATE TABLE IF NOT EXISTS Fast_Meals(meal_id SERIAL PRIMARY KEY , meal_name text,price numeric);")
        cursor.execute("CREATE TABLE IF NOT EXISTS Fast_Order(order_id  SERIAL PRIMARY KEY ,user_id int  REFERENCES Users (user_id) ON UPDATE CASCADE ON DELETE RESTRICT,meal_id int  REFERENCES Fast_Meals (meal_id));")
        connect.commit()
        connect.close
        

