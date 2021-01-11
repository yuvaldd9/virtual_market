from handlers import Server
from databases import database_handler as db
from common import GLOBALS


IP = '0.0.0.0'
PORT = 8080
DB_DIR = r"C:\Users\yuval\Desktop\School\Cyber - 2020-21\Prac\opp_prac\databases"
def main():
    server = Server(IP, PORT)
    server.start()


    
if __name__ == "__main__":
    db_cmds = [
        ('users',"""CREATE TABLE users(name TEXT, user_id INTEGER, pwd TEXT, money INTEGER)"""), #users db
        ('sells',"""CREATE TABLE sells(seller TEXT, buyer TEXT, product_id INTEGER)"""), #sells db
        ('marketplace',"""CREATE TABLE marketplace(name TEXT, description TEXT, seller TEXT, price INTEGER, product_id INTEGER)"""),#marketplace db
        ('questions',"""CREATE TABLE questions(_from TEXT, _to TEXT, question TEXT)""")
    ]

    for db_name,cmd in (db_cmds):
        dir = "%s\\%s.db"%(DB_DIR,db_name)
        GLOBALS.db_dir[db_name] = dir
        db.connect_dataBase(dir, cmd)
    
    main()