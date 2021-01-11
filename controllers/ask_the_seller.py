from controller import controller
from ..common import Request, Response, Codes, Statuses, GLOBALS
from ..databases import database_handler as db


@controller(Codes.ASK_THE_SELLER)
def ask_the_seller(args):
    status = Statuses.SUCCESS
    product_id = args['product_id']
    question = args['question']
    user_id = args['jwt']
    product_seller_id = (db.get_data(GLOBALS.db_dir['marketplace'],\
        """SELECT user_id FROM marketplace WHERE product_id = """ + str(product_id)))[0]

    if not (db.set_data(GLOBALS.db_dir['questions'], """INSERT INTO questions(_from, _to, question) VALUES(?,?,?)"""\
                                            , (user_id, product_seller_id, question))):
    
        status = Statuses.BAD_REQUEST
    
    return Response(status)