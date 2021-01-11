from controller import controller
from ..common import Request, Response, Codes, Statuses, GLOBALS
from ..databases import database_handler as db
import hashlib

@controller(Codes.REGISTER)
def register(args):
    status = Statuses.SUCCESS
    username = args['name']
    password = args['password']
    print db.set_data(GLOBALS.db_dir['users'], """INSERT INTO users(name, user_id, pwd, money) VALUES(?,?,?,?)""", (username, GLOBALS.USER_ID, str(hashlib.md5((password))), 1000))
    print ('[+] registered %s successfully') % (username)
    GLOBALS.USER_ID += 1
    return Response(status, jwt = GLOBALS.USER_ID-1)
