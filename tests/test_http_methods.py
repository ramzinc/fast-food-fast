import pytest
import json
from api.viewhandle import app
import unittest

class testCases(unittest.TestCase):
        def setUp(self):
            test_client = app.test_client()
            app.config['TESTING'] = True

        #@pytest.fixture
        #def request_client(self):
         #   test_client = app.test_client()
          #  app.config['TESTING'] = True
            
            
 #           bad_data = {'orders':[{"items":[{"kawunga":1000,"emboli":2000,"supu":1000}],"done":False}]}
#
  #          return test_client
            
        def test_index_page(self,request_client):

            req_response = request_client.get('/')
            assmsg = b'<p><h4>Follow the <a href=https://fast-food-fast-mpiima.herokuapp.com/api/v1/orders/> to the API </a><h4></p>'
            assert assmsg == req_response.data
            

        def test_get_orders(request_client):
            saved_data = [{"meal_name": "kawunga","price":1000},{"meal_name":"cat","price":1000},
                            {"meal_name":"frog","price":1000}]
            req_response = request_client.get('/api/v1/orders/').get_json()
            assert saved_data == req_response
        def test_get_specific_order(request_client):
            order = {"meal_name": "kawunga","price":1000,"status":False}
            ret_order = request_client.get('/api/v1/orders/1').get_json()
            assert order == ret_order

        def test_update_order(request_client):
            saved_data = [{"meal_name": "kawunga","price":1000},{"meal_name":"cat","price":1000},
                            {"meal_name":"frog","price":1000}]
            return_msg = "Message:Order Created [{'id': 1, 'meal_name': 'kawunga', 'price': 1000, 'status': False}, {'id': 2, 'meal_name': 'cat', 'price': 1000, 'status': False}, {'id': 3, 'meal_name': 'frog', 'price': 1000, 'status': False}]"
            
            ret_order = request_client.post('/api/v1/orders/',json=saved_data)
            ret = ret_order.get_json()
            #saved_data = json.dumps(saved_data) No need to cast the saved_data into json
            #import pdb; pdb.set_trace()
            assert  return_msg == ret 


        #def test_update_status(request_client):
        #   test_data = {'id': 1,'items': [{'rice':  10000,'matooke':4000,'chickentika':6000}],'done':True}
            #  response_status = request_client.put('/api/v1/orders/1')
        # out = response_status.get_json()
            #assert out == test_data

