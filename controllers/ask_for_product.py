from controller import controller
from ..common import Request, Response, Codes, Statuses, GLOBALS
from ..databases import database_handler as db


@controller(Codes.ASK_FOR_DETAILS)
def ask_for_product(args):
    status = Statuses.SUCCESS
    product_id = args['product_id']
    try:
        product_name ,description, price = (db.get_data(GLOBALS.db_dir['marketplace'], """SELECT product_name ,description, price FROM marketplace WHERE product_id = """ + str(product_id)))[0]
        return Response(status, price = int(price), description = description, product_name = product_name)
    except:
        status = Statuses.BAD_REQUEST
        return Response(status)