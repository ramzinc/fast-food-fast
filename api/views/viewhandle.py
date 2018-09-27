from flask import Flask,request,make_response,jsonify
from flask_restful import Resource, Api
from api.models.model import Orders
from api.http_helper_scripts import validate
class Requests_Handler(Resource):
    app = Flask(__name__)
    api = Api(app)
    id = 0
    def get(self):
        return Orders.get_order_json

    def post(self):
        posted_order= request.get_json()
        if validate(posted_order):
            posted_order['id'] = id + 1
            order = Orders(posted_order['id'],posted_order['meal_name'],posted_order['price'],False)
            resp = make_response(jsonify(order),200)
            return resp

app = Flask(__name__)
api = Api(app)
api.add_resource(Requests_Handler,"/api/v1/")
if __name__ == '__main__':
    app.run()
