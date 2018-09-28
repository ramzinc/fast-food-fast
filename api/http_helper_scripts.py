#rom api.models.model import Orders
from api.model import Orders
#orders = [{'id': 1,'meal_name':'matooke' ,'price':4000},{'id':2,'meal_name':'chickentika','price':6000,'status': False},
#                   {'id': 3,'meal_name': 'beans' ,'price':1000, 'status': False}]

#validate if there no id , and a string of meal_name and price is an int
def validate(order):
    for i in order:
        if 'id' not in i and 'meal_name' in i and 'price' in i and isinstance(i['price'],int):
           # import pdb;pdb.set_trace()
            return True
        else:
           # import pdb;pdb.set_trace()
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


def insert_data(ps_order,id):
    id =  int(id)
    order = list()
    for i in ps_order:
        id = id + 1
        order.append(Orders(id,i['meal_name'],i['price'],False).get_order_json())
        continue
    #import pdb; pdb.set_trace()
    return order        

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