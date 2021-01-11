from controller import controller
from ..common import Request, Response, Codes, Statuses, GLOBALS
from ..databases import database_handler as db


@controller(Codes.CHANGE_DESCRIPTION)
def change_description(args):
    status = Statuses.SUCCESS
    product_id = args['product_id']
    new_description = args['new_description']
    user_id = args['jwt']
    product_seller_id = (db.get_data(GLOBALS.db_dir['marketplace'],"""SELECT user_id FROM marketplace WHERE product_id = """ + str(product_id)))[0]
    if user_id == product_seller_id:
        db.set_data(GLOBALS.db_dir['marketplace'], """UPDATE marketplace SET description = """ + str(new_description)+""" WHERE product_id ="""+str(product_id))
    else:
        status = statuses.BAD_REQUEST
    return Response(status)
