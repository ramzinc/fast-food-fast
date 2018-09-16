from flask import Flask,jsonify,request,make_response
import json
app = Flask(__name__)
ORDER_ID_PRESENT_FLAG = False
orders = {'orders':[{'id': 1,'items': [{'rice':  10000,'matooke':4000,'chickentika':6000}]},
                    {'id': 2,'items': [{'naan':6000,'beans':1000,'posho': 500}]}
    
]}

@app.route('/',methods=['GET'])
def get_index():

    return '../ui-templates/index'


@app.route('/orders/',methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders/',methods=['POST']) 
def update_order():
    order = request.get_json()
    if validate(order):
        #append the list of orders
        for x in order['orders']:
            response = orders['orders'].append(x)
        ret = json.dumps(orders) #typecast dict to json
        #Tell The client that the output is json
        content_type = [('Content-Type','application/json')]
        return (ret,201,content_type)
    else:
        response = ("The Order Was Malformed",400)
        return response
    
#validate if there is an id , items and that the items is of a list type
def validate(order):
    for i in order['orders']:
        if 'id' in i and 'items' in i and isinstance(i['items'],list) and check_id(i['id']):
            return True
        else:
            return False

def check_id(num):
    for i in orders["orders"]:
        #import pdb; pdb.set_trace()
        if num == i["id"]:
           ORDER_ID_PRESENT_FLAG = True 
           return False
        else:
           continue
    return True