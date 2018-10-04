import pytest
import json
from api.controllers.viewhandle import app,ret_order
import unittest
from flask import jsonify
from api.models.database import Database
class testCases(unittest.TestCase):
#        def setUp(self):
#            self.test_client = app.test_client()
#            app.config['TESTING'] = True
#            #post_data = [{"meal_name": "kawunga","price":1000},{"meal_name":"cat","price":1000},{"meal_name":"frog","price":1000}]
#            post_data ={"meal_name": "kawunga","price":1000}
#            self.test_client.post(':5000/api/v1/orders',data=json.dumps(post_data)


#ave_data = {'items':[{'id':1,'meal_name':"mawolu","price":4000,"status":False}


    def test_client():
         db_name="fast_food_fast_testing"
         db = Database(db_name)
         with db.connect_datab() as db_conn:
              cur = db_conn.cursor()
              cur.execute_query


  

         #post_data = {"meal_name": "kawunga","price":1000}
         test_client = app.test_client()
         app.config['TESTING'] = Tre

         #saved_data = test_client.post('/api/v1/orders',dat)
         #saved_data = test_client.post('/api/v1/orders',data=post_data, follow_redirects=True)         
         return test_cliet

      def test_index_page(test_client):
         req_response = test_client.get('/api/v1/')
           assmsg = b'Follow Me'
           assert assmsg in req_response.data            

        def test_get_orders(test_client):

            #res = test_client.post('/api/v1/orders/',data=post_data)            
            req_response = test_client.get('/api/v1/orders/').get_json()
            global save_data

            assert req_response == save_data
            #request_data = test_client.post('/api/v1/orders',data=post_data)
            #assert req_response== res
               #self.assertEqual(post_data,req_response)

        def test_get_specific_order(test_client):
            order = {'id':1,'meal_name':"mawolu","price":4000,"status":False}
            ret_order = test_client.get('/api/v1/orders/1').get_json()      
            assert order == ret_order


        def test_update_order(test_client):
             #  saved_data = jsonify(saved_data)
            post_data = {"meal_name": "Food","price":1000}
            ret_order = test_client.post('/api/v1/orders/',json=post_data)
            match = {
            "items": {
                "id": 2,
                "meal_name": "Food",
                "price": 1000,
                "status": False
            }
        }
            ret = ret_order.get_json()
               #    #import pdb; pdb.set_trace()
            assert  ret == match 

        def test_update_status(test_client):
               #   test_data = {'id': 1,'items': [{'rice':  10000,'matooke':4000,'chickentika':6000}],'done':True}
                response_status = test_client.put('/api/v1/orders/1')
                save_data = {'id':1,'meal_name':"mawolu","price":4000,"status":True}
                out = response_status.get_json()
                assert out == save_data

