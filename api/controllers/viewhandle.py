from flask import Flask,request,make_response,jsonify,g
from flask_restful import Resource, Api
from api.models.model import Orders
from api.http_helper_scripts import validate ,insert_data,check_if_list,get_order,check_id_present,change_status
import json
id = 0
app = Flask(__name__)
app.config.from_object('configapp.Config')
#DATABASE_URI = app.config['DATABASE_URI']
api = Api(app)
ret_order = list()
#ret_order =  [{'id':1,'meal_name':"mawolu","price":4000,"status":False}]
class Requests_Handler(Resource):
    '''
    This class handles the post method requests
    '''
    app = Flask(__name__)
    api = Api(app)
   
    order =  list()
    
    def post(self):
        req_data = request.get_json()
       # if check_if_list(req_data):
       #     posted_order = req_data
       # else:
       #     posted_order = list()
       #     posted_order.append(req_data)
        #import pdb;pdb.set_trace()
        if validate(req_data):
            
            #import pdb;pdb.set_trace()
            # The id will be incremented by the insert_data function 
            # 
            #global id     
            global ret_order
            ret_order = insert_data(req_data,ret_order) 
            #import pdb;pdb.set_trace()
            #ret_order.append(self.order)
            ret_order_local = ret_order[id-1]
            #resp = make_response(json.dumps(self.order),200,[('Content-Type','application/json')])
            #msg_resp = make_response(ret_order_local,201)
            return make_response(jsonify({"items":ret_order_local}),201)
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
        
        #list_data = insert_data("meal_name",4)
        global ret_order
        ret_o = ret_order
        #if list_data:
        #    return (jsonify({'message': list_data}),200)
    #
        #resp = make_response(ret,200)
       # import pdb;pdb.set_trace()
        mime_type =("Content-Type","application/json")
        return make_response(jsonify({"items":ret_o}), 200)

class Get_Request(Resource):
    
    def get(self,id):
        global ret_order
        if check_id_present(id,ret_order):
            return (get_order(id,ret_order),200)
        else:
            return ("{'Message': 'ID Not Found'}",404)

class Get_Index(Resource):

    def get(self):
        #msg = '<p><h4>Follow the <a href=https://fast-food-fast-mpiima.herokuapp.com/api/v1/orders/> to the API </a><h4></p>'
        msg = 'Follow Me'
        return (msg,200)

class Put_Status(Resource):
    
    def put(self,id):
        if check_id_present(id,ret_order):
            order = get_order(id,ret_order)
            order['status']=change_status(order['status'])
            return (order,200)
        else:
            return make_response("Order Does not exist",200)

api.add_resource(Requests_Handler,"/api/v1/orders/")
api.add_resource(Get_Requests,"/api/v1/orders/")
api.add_resource(Get_Request,"/api/v1/orders/<int:id>")
api.add_resource(Get_Index,"/api/v1/")
api.add_resource(Put_Status,"/api/v1/orders/<int:id>")
if __name__ == '__main__':
        app.run()
