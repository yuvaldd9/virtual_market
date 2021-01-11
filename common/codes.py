class Codes(object):
    # Server Broadcast Messages Codes
    
    REGISTER = "register"
    LOGIN = "sign_in"

    # Requests Codes
    UPLOAD_PRODUCT = 'upload_product'
    CHANGE_PRICE = 'change_price'
    CHANGE_DESCRIPTION = 'change_description'
    CHANGE_NAME = 'change_name'
    CANCEL_SELL = 'cancel_sell'

    ASK_FOR_DETAILS = 'ask_for_details'
    COMPLAIN = 'complain'
    BUY = 'buy'
    ASK_THE_SELLER = 'ask_the_seller'
    CANCEL_BUY = 'cancel_buy'

    CHECK_FOR_QUESTIONS = 'check_for_questions'
    CHECK_FOR_SELLS = 'check_for_sells'
    
class Statuses(object):
    # General Statuses
    SUCCESS = 'success'
    BAD_REQUEST = 'bad_request'
    DENIED = 'denied'
    NOT_FOUND = 'not_found'
    CONFLICT = 'conflict'

class GLOBALS(object):
    USER_ID = 0
    PRODUCT_ID = 0
    db_dir = {}
