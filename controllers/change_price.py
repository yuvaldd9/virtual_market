from controller import controller
from ..common import Request, Response, Codes, Statuses, GLOBALS
from ..databases import database_handler as db


@controller(Codes.CHANGE_PRICE)
def change_price(args):
    status = Statuses.SUCCESS
    product_id = args['product_id']
    price = args['new_price']
    user_id = args['jwt']
    product_seller_id = (db.get_data(GLOBALS.db_dir['marketplace'],\
         """SELECT user_id FROM marketplace WHERE product_id = """ + str(product_id)))[0]
    if user_id == product_seller_id:
        db.set_data(GLOBALS.db_dir['marketplace'], """UPDATE marketplace SET price = """ + str(price)+""" WHERE product_id ="""+str(product_id))
    else:
        status = statuses.BAD_REQUEST
    return Response(status)
