from controller import controller
from ..common import Request, Response, Codes, Statuses, GLOBALS
from ..databases import database_handler as db
import hashlib

@controller(Codes.UPLOAD_PRODUCT)
def upload_product(args):
    status = Statuses.SUCCESS
    product_name = args['product_name']
    price = args['price']
    description = args['description']
    user_id = args['jwt']
    if not db.set_data(GLOBALS.db_dir['marketplace'], """INSERT INTO marketplace(product_name ,description, seller, price, product_id)\
                                 VALUES(?,?,?,?,?)""", (product_name,description, user_id, price, GLOBALS.PRODUCT_ID )):
        status = Statuses.BAD_REQUEST
    GLOBALS.PRODUCT_ID += 1
    
    return Response(status, product_id = GLOBALS.PRODUCT_ID - 1)

