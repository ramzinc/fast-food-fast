from flask import Flask,request,make_response,jsonify,g
from flask_restful import Resource, Api
from api.model import Orders
from api.http_helper_scripts import validate ,insert_data,check_if_list,get_order,check_id_present
import json

app = Flask(__name__)
api = Api(app)
ret_order = dict()
class Requests_Handler(Resource):
    app = Flask(__name__)
    api = Api(app)
    id = 0
    order =  list()
    
    def post(self):
        req_data = request.get_json()
        if check_if_list(req_data):
            posted_order = req_data
        else:
            posted_order = list()
            posted_order.append(req_data)
        #import pdb;pdb.set_trace()
        if validate(posted_order):
            
            #posted_order[1]['id'] = id + 1
            # Orders(posted_order['id'],posted_order['meal_name'],posted_order['price'],False)
            #import pdb;pdb.set_trace()
            # The id will be incremented by the insert_data function that will loop through the list 
            self.order = insert_data(posted_order,self.id) 
            #import pdb;pdb.set_trace()
            global ret_order 
            ret_order= self.order
            ret_order_local = ret_order
            #resp = make_response(json.dumps(self.order),200,[('Content-Type','application/json')])
            msg_resp = make_response('Message:Order Created {0}'.format(ret_order_local),201)
            return msg_resp
        else:
            return make_response('Message: The Structure Is Malformed',400)

    
    @app.errorhandler(405)
    def url_not_found(self, error):
        return make_response(jsonify({'message':'Requested method not allowed'}), 405)

    @app.errorhandler(404)
    def page_not_found(self,error):
        return make_response(jsonify({'message':'page not found, check the url'}), 404)

    @app.errorhandler(500)
    def internal_error(self,error):
         return make_response(jsonify({'message':"500 error"}),500)


class Get_Requests(Resource):
    def get(self):
        #ret_o = dict()
        global ret_order
        ret_o = ret_order

       
        #resp = make_response(ret,200)
       # import pdb;pdb.set_trace()
        return ('These are the orders{0}'.format(ret_o),200)

class Get_Request(Resource):
    
    def get(self,id):
        global ret_order
        if check_id_present(id,ret_order):
            return (get_order(id,ret_order),200)
        else:
            return ("{'Message': 'ID Not Found'}",404)

class Get_Index(Resource):

    def get(self):
        msg = '<p><h4>Follow the <a href=https://fast-food-fast-mpiima.herokuapp.com/api/v1/orders/> to the API </a><h4></p>'
        return msg



api.add_resource(Requests_Handler,"/api/v1/orders/")
api.add_resource(Get_Requests,"/api/v1/orders/")
api.add_resource(Get_Request,"/api/v1/orders/<int:id>")
api.add_resource(Get_Index,"/api/v1")
if __name__ == '__main__':
        app.run()
