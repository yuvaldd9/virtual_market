from controller import controller
from ..common import Request, Response, Codes, Statuses, GLOBALS
from ..databases import database_handler as db
import hashlib

@controller(Codes.LOGIN)
def register(args):
    status = Statuses.SUCCESS
    username = args['name']
    password = args['password']
    user_real_pwd, user_id = (db.get_data(GLOBALS.db_dir['users'], """SELECT pwd, user_id FROM users WHERE username = """ + username))

    if hashlib.md5(bytes(password)) == user_real_pwd:
        print ('[+] %s login successfully') % (username)
        return Response(status, jwt = user_id)
    else:
        status = Statuses.NOT_FOUND
        return Response(status)