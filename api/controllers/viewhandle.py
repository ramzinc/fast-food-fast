from flask import Flask,request,make_response,jsonify,g
from flask_restful import Resource, Api,reqparse
from flask_jwt_extended import (JWTManager,jwt_required,create_access_token,get_jwt_identity)
from api.models.orders import Orders
from api.models.users import User
from api.http_helper_scripts import validate_status,validate_food ,insert_data,check_if_list,get_order,check_id_present,change_status
from api.user_helper_scripts import (is_admin,validate_user, insert_user_data_into_userdb,get_menu_items,validate_signin_data,get_user_data,get_orders,get_specific_order)
import json

#id = 0
app = Flask(__name__)
app.config.from_object('configapp.Config')
app.env= 'Development'
app.config['JWT_SECRET_KEY']= 'ZMv_k_%;8-7-6ZHnCub'
api = Api(app)
jwt = JWTManager(app)
ret_order = list()
class Post_Food_Item(Resource):
    '''
    This class handles the post method requests
    '''
   #app = Flask(__name__)
   #api = Api(app)
    
    
    
    def post(self):
        '''
        Method adds the The Food Item to the database
        '''
        req_data = request.get_json()
        #import pdb;pdb.set_trace()
        if validate_food(req_data):
            
            food_item =  list()
            insert_data(req_data,food_item) 
            #import pdb;pdb.set_trace()
            #ret_order.append(self.order)
            ret_order_local = req_data
            #resp = make_response(json.dumps(self.order),200,[('Content-Type','application/json')])
            #msg_resp = make_response(ret_order_local,201)
            return make_response(jsonify({"Menu Item Added":ret_order_local}),201)
        else:
            return make_response(jsonify({'Message': 'meal_name parmater missing'}),400)

        parser = reqparse.RequestParser()
        parser.add_argument('meal_name',type=str ,required=True,help={'Missing Field: The meal_name Is Required {error_msg}'})
        

    

class Get_Menu(Resource):
    def get(self):
 
        menu_list = get_menu_items()
        return make_response(jsonify({"items":menu_list}),200)
        
        

class Get_Index(Resource):
    ''' 
    Returns The Index Page
    '''
    def get(self):
        #msg = '<p><h4>Follow the <a href=https://fast-food-fast-mpiima.herokuapp.com/api/v1/orders/> to the API </a><h4></p>'
        msg = 'Follow Me'
        return make_response(msg,200)

class Put_Status(Resource):
    '''
    Class deals with the put status to /orders/<order_id:int>
    '''
    @jwt_required
    def put(self,order_id):
        '''
        Put Method EndPoint Changes order_status of order
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('order_id',type=int,help='Error Msg:Your order_id does not exist',required=True)
        
        req_status  = request.get_json()
        current_user_id = get_jwt_identity()
        user =User()
        user_info = user.get_user_data_using_id(current_user_id)
        if user.validate_admin(user_info) and validate_status(req_status)and check_id_present(order_id):
            response_text = change_status(req_status['status'],order_id)
            return response_text
        else:
            return make_response(jsonify({"Error_msg":"Your request contains errors probably not an Admin or Id doesnot exis or status is illegal"}),400)

        
class Post_Signup(Resource):
    '''
    Sign Up Api Endpoint
    '''
    def post(self):
        req_data = request.get_json()
        usr = User()
        #parser = reqparse.RequestParser()
        #parser.add_argument('email',type=str,required=True,help='Error_Msg: Your email is not a being passed as a string.')
        #parser.add_argument('first_name',type=str,required=True,help='Error_MSg: Missing first_name or it is not a string {error_msg}')
        #parser.add_argument('last_name',type=str,required=True,help='Error_MSg: Missing last_name or it is not a string {error_msg}')
        #parser.add_argument('email',type=str,required=True,help='Error_MSg: Missing email or it is not a string {error_msg}')
        #parser.add_argument('password',type=str,required=True,help='Error_MSg: Missing password or it is not a string {error_msg}')
        #req_data = parser.parse_args()
        ret_msg = usr.check_if_user_exists(req_data)
        if ret_msg == '':
            return make_response(jsonify({"Error_msg":"Email Already Exists"}))
        if validate_user(req_data) and ret_msg == True:
            insert_user_data_into_userdb(req_data)
            response_string ={"user_entered":req_data}
            content = ('Content-Type','applicaton/json')
            return make_response(jsonify(response_string),200)
        else:
            return make_response(jsonify({"Error_msg":"Your Data please check that you have a valid email and string objects for the rest of the parameters is wrong"}),400)

        

class Post_SignIn(Resource):
    '''
    Sign in into the app  
    '''
    def post(self):
        req_data = request.get_json()
        if validate_signin_data(req_data):
            db_data = get_user_data(req_data)
            access_token = create_access_token(identity=db_data['id'],expires_delta=False)
            return jsonify(access_token=access_token)
        else:
            return make_response(jsonify({'One of your inputs are invalid'}))

class Post_Order(Resource):
    '''
    Method to post order
    '''
    @jwt_required
    def post(self):
        '''
        Protected Endpoint that posts an order. Only logged in Users can use it POST /users/orders
        '''
        current_user = get_jwt_identity()
        req_data = request.get_json()
        meal_name = req_data['meal_name']
        ord = Orders(meal_name,current_user)
        ord.set_meal_id()
        ord.set_status('New')
        quantity = ord.get_quantity()
        if quantity > 1:
             ord.save_quantity_alone()        
        else:
             ord.save_into_db()
        order = ord.get_order_dic()
        return make_response(jsonify({'order_place':order}))

class Get_List_Orders(Resource):
    '''
    Api EndPoint to get list of orders GET /orders/
    '''
    @jwt_required
    def get(self):
        current_user_id = get_jwt_identity()
        user =User()
        user_info = user.get_user_data_using_id(current_user_id)
        if user.validate_admin(user_info):
            order = get_orders()
            return make_response(jsonify({"order":order}))
        else:
            return make_response(jsonify({"Msg":"Your Not Authorised to get dat list"}),401)
        
class Get_User_Order(Resource):
    '''
    Get A Specific user's order id Only Accessible by Admin
    '''
    @jwt_required
    def get(self):
        login_id = get_jwt_identity()
        usr = User()
        #import pdb;pdb.set_trace()
        #usr_info = 
        if usr.check_if_user_id_indb(login_id):
            meal_names = usr.check_for_specific_usr_ord(login_id)
            if meal_names == []:
                return make_response(jsonify({"Msg":"Your User Has No Orders"}))
            else:
            #import pdb; pdb.set_trace()
                return make_response(jsonify({"ordered_meals": meal_names}))
        else:
            return make_response(jsonify({"Error_Msg":"You are not Authorized to access this p"}))

class Get_Specific_Order(Resource):
    '''
    Class To get Specific Order
    '''
    @jwt_required
    def get(self,order_id):
        id  = get_jwt_identity
        current_user_id = get_jwt_identity()
        user =User()
        user_info = user.get_user_data_using_id(current_user_id)
        if user.validate_admin(user_info):
            meal_name = get_specific_order(order_id)
            return make_response(jsonify({"The order is ":meal_name}),200)
        elif not check_id_present(order_id):
            return make_response(jsonify({"The order ID is not Present In The DB":order_id}),404)
        else:
            return make_response(jsonify({"Error_Msg":"You are not athorized"}))
    
    @app.errorhandler(500)
    def get_none_type_error(self,error):
        return make_response(jsonify({"Not Found":"The order You Entered is not there"}))



api.add_resource(Post_Signup,"/auth/signup")
api.add_resource(Post_SignIn,"/auth/login")
api.add_resource(Post_Food_Item,"/menu")
api.add_resource(Get_Menu,"/menu")
api.add_resource(Post_Order,"/users/orders")
api.add_resource(Get_User_Order,"/users/orders")
api.add_resource(Get_List_Orders,"/orders")
api.add_resource(Get_Specific_Order,"/orders/<int:order_id>")
api.add_resource(Get_Index,"/api/v1/")
api.add_resource(Put_Status,"/orders/<int:order_id>")

@app.errorhandler(TypeError)
def none_type_error(error):
    return make_response(jsonify({'Error_msg':'The data you entered does not exist'} ))
if __name__ == '__main__':
        app.run()
