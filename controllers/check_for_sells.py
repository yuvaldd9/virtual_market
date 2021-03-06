from controller import controller
from ..common import Request, Response, Codes, Statuses, GLOBALS
from ..databases import database_handler as db


@controller(Codes.CHECK_FOR_SELLS)
def check_for_sells(args):
    status = Statuses.SUCCESS
    user_id = args['jwt']
    product_seller_id = (db.get_data(GLOBALS.db_dir['marketplace'],"""SELECT user_id FROM marketplace WHERE product_id = """ + str(product_id)))[0]
    
    if user_id == product_seller_id:
        try:
            sells = (db.get_data(GLOBALS.db_dir['sells'], """SELECT * FROM sells WHERE seller = """ + str(product_id)))[0]
        except:
            status = Statuses.BAD_REQUEST
    else:
        status = statuses.BAD_REQUEST
    return Response(status)
