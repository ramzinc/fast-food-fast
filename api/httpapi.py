from flask import Flask,jsonify,request,make_response
import json
app = Flask(__name__)
#ORDER_ID_PRESENT_FLAG = False
orders = {'orders':[{'id': 1,'items': [{'rice':  10000,'matooke':4000,'chickentika':6000}],'done':False},
                    {'id': 2,'items': [{'naan':6000,'beans':1000,'posho': 500}], 'done':False}
    
]}

@app.route('/',methods=['GET'])
def get_index():

    return '<p><h4>Follow the <a href=https://fast-food-fast-mpiima.herokuapp.com/orders/> to the API </a><h4></p>'


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


@app.route('/orders/<int:order_id>',methods=['GET'])
def get_specific_order(order_id):
    if check_id_present(order_id):
        content_type = [('Content-Type','application/json')]
        ret = json.dumps(orders['orders'][order_id-1])
        return (ret,200,content_type)
    else:
        return '<p>The Order You Have entered Is InValid.</p>'

@app.route('/orders/<int:order_id>',methods=['PUT'])
def update_status(order_id):
   if check_id_present(order_id):
      #request_order = request.get_json()
      order_status = orders['orders'][order_id-1]['done']
      new_order_status = change_status(order_status)
      orders["orders"][order_id-1]['done'] = new_order_status
      content_type = [('Content-Type','application/json')]
      ret = json.dumps(orders['orders'][order_id-1])
      content_type = [('Content-Type','application/json')]
      return (ret,200,content_type)

#HELPER SCRIPTS     
def change_status(order_status):
    if order_status == False:
        return True
    else:
        return False

#validate if there is an id , items and that the items is of a list type
def validate(order):
    for i in order['orders']:
        if 'id' in i and 'items' in i and isinstance(i['items'],list) and not check_id_present(i['id']):
            return True
        else:
            return False

#
def check_id_present(num):
    for i in orders["orders"]:
        #import pdb; pdb.set_trace()
        if num == i["id"]:
           #ORDER_ID_PRESENT_FLAG = True 
           
           return True
        else:
           continue
    return False