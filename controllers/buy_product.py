from controller import controller
from ..common import Request, Response, Codes, Statuses, GLOBALS
from ..databases import database_handler as db


@controller(Codes.BUY)
def change_name(args):
    status = Statuses.SUCCESS
    product_id = args['product_id']
    user_id = args['jwt']
    product_seller_id = (db.get_data(GLOBALS.db_dir['marketplace'],\
         """SELECT user_id FROM marketplace WHERE product_id = """ + str(product_id)))[0]
    
    if user_id == product_seller_id:
        db.set_data(GLOBALS.db_dir['sells'], """INSERT INTO sells(seller, buyer, product_id) VALUES(?,?,?)""", (product_seller_id, user_id, product_id))
        buyer_money = (db.get_data(GLOBALS.db_dir['users'], """SELECT money FROM users WHERE user_id = """ + str(user_id)))[0]
        seller_money = (db.get_data(GLOBALS.db_dir['users'], """SELECT money FROM users WHERE user_id = """ + str(product_seller_id)))[0]
        product_price = (db.get_data(GLOBALS.db_dir['marketplace'], """SELECT price FROM users WHERE product_id = """ + str(product_id)))[0]

        try:
            db.set_data(GLOBALS.db_dir['users'], """UPDATE users SET money = """+str(int(buyer_money) - int(product_price))+""" WHERE user_id = """+str(user_id))
            db.set_data(GLOBALS.db_dir['users'], """UPDATE users SET money = """+str(int(seller_money) + int(product_price))+""" WHERE user_id = """+str(product_seller_id))
        except:
            status = Statuses.BAD_REQUEST
    else:
        status = statuses.BAD_REQUEST
    return Response(status)
