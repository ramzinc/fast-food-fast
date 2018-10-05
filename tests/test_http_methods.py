import pytest
import os
import json
from api.controllers.viewhandle import app,ret_order
import unittest
from flask import jsonify
from api.models.database import Database
class testCases(unittest.TestCase):

        db_name = os.getenv("DATABASE_TESTING") 
        def setUp(self):
            signup_data = {"first_name":"Arnold","last_name":"Mpiima","admin":True,"email":"admin@admin.com","password":"12345"}
            
            self.test_client = app.test_client()
            test_post = self.test_client.post("/auth/signup",data=json.dumps(signup_data),content_type="application/json").get_json()
            app.config['TESTING'] = True
            db = Database()
            db.execute_query()

            
        def tearDown(self):
            db  = Database()
            db.drop_tables()            

        def test_index_page(self):
            req_response = self.test_client.get('/api/v1/')
            assmsg = b'Follow Me'
            self.assertEquals(assmsg,req_response.data)

        def test_post_sign_up(self):
            post_signup_data = {"first_name":"Arnold","last_name":"Mpiima","admin":True,"email":"mpiima@admin2.com","password":"12345"}
            post_signd = json.dumps(post_signup_data)
            req_response = self.test_client.post('/auth/signup',data=post_signd,content_type="application/json").get_json()
            saved_data = json.dumps({'user_entered':post_signup_data})
            resp = json.dumps(req_response)
            self.assertIn("user_entered",saved_data)


        def test_post_login(self):
            login = {"email":"admin@amdin.com","password":"123456"}
            token = self.test_client.post("/auth/login",data=json.dumps(login),content_type="application/json").data
            self.assertIn("access_token",token)

        def test_get_specific_order(self):
            order = {'id':1,'meal_name':"mawolu","price":4000}
            ret_order = self.test_client('/orders/1').get_json()      
            assert order == ret_order
#
#
    #    def test_update_order(test_client):
    #         #  saved_data = jsonify(saved_data)
    #        post_data = {"meal_name": "Food","price":1000}
    #        ret_order = test_client.post('/api/v1/orders/',json=post_data)
    #        match = {
    #        "items": {
    #            "id": 2,
    #            "meal_name": "Food",
    #            "price": 1000,
    #            "status": False
    #        }
    #    }
    #        ret = ret_order.get_json()
    #           #    #import pdb; pdb.set_trace()
    #        assert  ret == match 
#
    #    def test_update_status(test_client):
    #           #   test_data = {'id': 1,'items': [{'rice':  10000,'matooke':4000,'chickentika':6000}],'done':True}
    #            response_status = test_client.put('/api/v1/orders/1')
    #            save_data = {'id':1,'meal_name':"mawolu","price":4000,"status":True}
    #            out = response_status.get_json()
    #            assert out == save_data