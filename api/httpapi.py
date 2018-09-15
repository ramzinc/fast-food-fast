from flask import Flask,jsonify
app = Flask(__name__)
orders = {'orders':[{'id': 1,'items': [{'rice':  10000,'matooke':4000,'chickentika':6000}]},
                    {'id': 2,'items': [{'naan':6000,'beans':1000,'posho': 500}]}
    
]}

@app.route('/',methods=['GET'])
def get_index():

    return '../ui-templates/index'


@app.route('/orders/',methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders',methods=['GET']) 
def update_order():
    return 'kdlfa'

@app.route('/orders/',methods=['PUT'])
def put_order():
    return "Its been put"

@app.route('/orders/',methods=[''])
def get_specific_order(order):
    return "Page with order"

@app.route('/orders/',methods=['GET'])
def update_order_status():
    return "ckkk"

