from api.models.model import Orders

#orders = [{'id': 1,'meal_name':'matooke' ,'price':4000},{'id':2,'meal_name':'chickentika','price':6000,'status': False},
#                   {'id': 3,'meal_name': 'beans' ,'price':1000, 'status': False}]

#validate if there no id , and a string of meal_name and price is an int
def validate(order):
    for i in order:
        if 'id' not in i and 'meal_name' in i and 'price' in i and isinstance(i['price'],int) and not check_id_present(i['id']):
            return True
        else:
            return False

def check_id_present(num,orders):
    for i in orders:
        #import pdb; pdb.set_trace()
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
