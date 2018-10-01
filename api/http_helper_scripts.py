#rom api.models.model import Orders
from api.models.model import Orders
#orders = [{'id': 1,'meal_name':'matooke' ,'price':4000},{'id':2,'meal_name':'chickentika','price':6000,'status': False},
#                   {'id': 3,'meal_name': 'beans' ,'price':1000, 'status': False}]

#validate if there no id , and a string of meal_name and price is an int
def validate(order):
    #for i in order:
    if 'id' not in order and 'meal_name' in order and 'price' in order and isinstance(order['price'],int):
        #import pdb;pdb.set_trace()
        return True
    else:
        #import pdb;pdb.set_trace()
        return False

def check_id_present(num,orders_list):
    for i in orders_list:
       # import pdb; pdb.set_trace()
        if num == i["id"]:
           #ORDER_ID_PRESENT_FLAG = True 
           
           return True
        else:
           continue
    return False

def change_status(order_status):
    if order_status == False:
        return True
    else:
        return False


def insert_data(ps_order,id,current_list):
    id =  int(id)
   # order = dict()
    id = id + 1
    current_list.append(Orders(id,ps_order['meal_name'],ps_order['price'],False).get_order_json())

    #import pdb; pdb.set_trace()
    return current_list ,id       

def check_if_list(lst):
    if isinstance(lst,list):
        return True
    else:
        return False

def get_order(id,order_list):
    for i in order_list:
        if i["id"] == id:
            return i
        continue