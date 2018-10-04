from flask import Flask,request,make_response,jsonify,g
from flask_restful import Resource, Api
from flask_jwt_extended import (JWTManager,jwt_required,create_access_token,get_jwt_identity)
from api.models.orders import Orders
from api.models.users import User
from api.http_helper_scripts import validate_food ,insert_data,check_if_list,get_order,check_id_present,change_status
from api.user_helper_scripts import (validate_user, insert_user_data_into_userdb,get_menu_items,validate_signin_data,get_user_data,get_orders)
import json

id = 0
app = Flask(__name__)
app.config.from_object('configapp.Config')
app.config['JWT_SECRET_KEY']= 'ZMv_k_%;8-7-6ZHnCub'
#DATABASE_URI = app.config['DATABASE_URI']
api = Api(app)
jwt = JWTManager(app)
ret_order = list()
#ret_order =  [{'id':1,'meal_name':"mawolu","price":4000,"status":False}]
class Post_Food_Item(Resource):
    '''
    This class handles the post method requests
    '''
   # app = Flask(__name__)
    #api = Api(app)
    
    
    
    def post(self):
        req_data = request.get_json()
       # if check_if_list(req_data):
       #     posted_order = req_data
       # else:
       #     posted_order = list()
       #     posted_order.append(req_data)
        #import pdb;pdb.set_trace()
        if validate_food(req_data):
            #global ret_order
            food_item =  list()
            insert_data(req_data,food_item) 
            #import pdb;pdb.set_trace()
            #ret_order.append(self.order)
            ret_order_local = req_data
            #resp = make_response(json.dumps(self.order),200,[('Content-Type','application/json')])
            #msg_resp = make_response(ret_order_local,201)
            return make_response(jsonify({"Menu Item Added":ret_order_local}),201)
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


class Get_Menu(Resource):
    def get(self):
        
        #list_data = insert_data("meal_name",4)
        #global ret_order
        #ret_o = ret_order
        menu_list = get_menu_items()
        #resp = make_response(ret,200)
        #import pdb;pdb.set_trace()
        #mime_type =("Content-Type","application/json")
        return make_response(jsonify({"items":menu_list}),200)

class Get_Request(Resource):
    @jwt_required    
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

class Post_Signup(Resource):
    def post(self):
        req_data = request.get_json()
        if validate_user(req_data):
            insert_user_data_into_userdb(req_data)
            return make_response(jsonify({"user_entered":req_data}))
        else:
            return make_response("One Of your values is wrong",400)        

class Post_SignIn(Resource):
    '''
    Sign in into the app  
    '''
    def post(self):
        req_data = request.get_json()
        if validate_signin_data(req_data):
            db_data = get_user_data(req_data)
            access_token = create_access_token(identity=db_data['id'],expires_delta=False)
            #import pdb;pdb.set_trace()
            #return make_response(jsonify({'Logged In As':db_data}),200)
            return jsonify(access_token=access_token)
        else:
            return make_response(jsonify({'One of your inputs are invalid'}))

class Post_Order(Resource):
    '''
    Method to post order
    '''
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        req_data = request.get_json()
        meal_name = req_data['meal_name']
        ord = Orders(meal_name,current_user)
        ord.set_meal_id()
        ord.set_status('New')
        #import pdb;pdb.set_trace() # Not running
        quantity = ord.get_quantity()
        if quantity > 1:
             ord.save_quantity_alone()        
        else:
             ord.save_into_db()
        order = ord.get_order_dic()
        return make_response(jsonify({'order_place':order}))

class Get_List_Orders(Resource):
    @jwt_required
    def get(self):
        current_user_id = get_jwt_identity()
        user =User()
        user_info = user.get_user_data_using_id(current_user_id)
        if user.validate_admin(user_info):
            order = get_orders()
            return make_response(jsonify({"order":order}))
        else:
            return make_response(jsonify({"Msg":"Your Not Authorised to get dat list"}))
        
#class Get_User_Order(Resource):
#    @jwt_required
#    def get(self):
#        customer_id = get_jwt_identity()


api.add_resource(Post_Signup,"/auth/signup")
api.add_resource(Post_SignIn,"/auth/login")
api.add_resource(Post_Food_Item,"/menu")
api.add_resource(Get_Menu,"/menu")
api.add_resource(Post_Order,"/users/orders")
#api.add_resource(Get_User_Order,"/users/orders")
api.add_resource(Get_List_Orders,"/orders")
api.add_resource(Get_Request,"/orders/<int:id>")
api.add_resource(Get_Index,"/api/v1/")
api.add_resource(Put_Status,"/api/v1/orders/<int:id>")
if __name__ == '__main__':
        app.run()
