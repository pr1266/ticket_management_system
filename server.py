#using postgre sql on port 5432

import os.path
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os
from binascii import hexlify
import tornado.web
from tornado.options import define , options
import psycopg2
import random
import json
import platform

define("port", default=1104, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:5432", help="database host")
define("mysql_database", default="network", help="database name")
define("mysql_user", default="postgres", help="database user")
define("mysql_password", default="postgres", help="database password")


USERNAME = PASSWORD = TOKEN = ""

conn = psycopg2.connect(user = "postgres",
                                  password = "postgres",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "network")

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            #POST METHODS :
            (r'/signup' , signup) ,
            (r'/login' , login) ,
            #(r'/logout' , logout) ,
            (r'/sendticket' , sendticket) ,
            (r'/closeticket' , closeticket) , 
            (r'/restoticketmod' , restoticketmod) ,
            (r'/changestatus' , changestatus) ,
            #GET OR POST :
            (r'/getticketcli' , getticketcli) ,
            (r'/getticketmod' , getticketmod) ,
            #DEFAULT URL :
            (r'.*' , defaulthandler) ,
        ]

        settings = dict()
        
        super(Application , self).__init__(handlers , **settings)
        self.db = conn.cursor()
        
class BaseHandler(tornado.web.RequestHandler):
    @property

    def db(self):
        return self.application.db

    def check_user(self , user):
        query = "select * from user_ where username = '{}'".format(user)
        resuser_ = self.db.execute(query)
        resuser = self.db.fetchone()
        #check if a user with this username exist or not
        if resuser:
            return True
        else:
            return False

    def check_api(self , api):
        resuser = self.db.execute("select * from user_ where api = '%s'" , api)
        #check for api existance
        if resuser:
            return True
        else:
            return False

    def check_auth(self , username , password):
        resuser = self.db.get("select * from user_ where username = '%s' and password_ = '%s'" , username , password)
        #check for user authentication
        if resuser:
            return True
        else:
            return False

class defaulthandler(BaseHandler):

    def get(self):
       output = {'status' : 'wrong command'}
       self.write(output)
    
    def post(self):
        output = {'status' : 'wrong command'}
        self.write(output)
    
class signup(BaseHandler):
    def post(self , *args , **kwargs):

        username = self.get_argument('username')
        password = self.get_argument('password')

        print(username , password)

        if not self.check_user(username):
            api_token = str(random.randint(200 , 40000))
            query = "insert into user_ (username , password_ , api , role_) values ('{}' , '{}' , '{}' , {})".format(username , password , str(api_token) , 0)
            print(query)
            self.db.execute(query)
            conn.commit()
            output = {'status' : 'True'}
            self.write(output)
        else:
            output = {'status' : 'False'}
            self.write(output)

class login(BaseHandler):

    def post(self , *args , **kwargs):

        username = self.get_argument('username')
        password = self.get_argument('password')

        query = "select * from user_ where username = '{0}' and password_ = '{1}'".format(username , password)
        print(query)
        response_ = self.db.execute(query)
        responses = self.db.fetchall()
        print(responses)
        if responses:

            for x in responses:
                id_ , Username , Password , Api , Role = x           
            TOKEN = Api
            ROLE = Role
            USERNAME = Username
            PASSWORD = Password
            
            output = {"status" : "True" , "api" : TOKEN , "role" : ROLE}
            self.write(output)
            pass
        else:
            output = {"status" : "False"}
            self.write(output)

class sendticket(BaseHandler):

    def post(self , *args , **kwargs):
        TOKEN = self.get_argument('api')
        #if self.check_api(TOKEN):
        body = self.get_argument('body')
        subject = self.get_argument('subject')
        response = ""
        query = "insert into ticket (sender , body , subject_ , response_ , status_) values('{}' , '{}' , '{}' , '{}' , {})".format(TOKEN , body , subject , response , 1)
        self.db.execute(query)
        conn.commit()
        #ticket_id_number += 1
        output = {"status" : "True"}
        self.write(output)
        

class getticketcli(BaseHandler):

    def post(self , *args , **kwargs):
        TOKEN = self.get_argument('api')
        #if self.check_api(TOKEN):
        print(TOKEN)
        query = "select * from ticket where sender = '{}'".format(TOKEN)
        response = self.db.execute(query)
        response_ = self.db.fetchall()
        print(response_)
        
        output = {
            "response" : response_ ,
        }
        self.write(output)


class closeticket(BaseHandler):

    def post(self , *args , **kwargs):
        api = self.get_argument('api')
        id = self.get_argument('id')
        #check_query = "select * from ticket where id = {} and sender = {}".format(id , api)
        query = "update ticket set status_ = 0 where sender = '{}' and id_ = {}".format(api , id)
        self.db.execute(query)
        conn.commit()
        output = {"status" : "True"}
        self.write(output)

class getticketmod(BaseHandler):

    def post(self , *args , **kwargs):
        api = self.get_argument("api")
        query = "select * from ticket"
        response = self.db.execute(query)
        response_ = self.db.fetchall()
        output = {"status" : "True" , "response" : response_}
        self.write(output)

class restoticketmod(BaseHandler):

    def post(self , *args , **kwargs):

        TOKEN = self.get_argument('api')
        body = self.get_argument('body')
        id = self.get_argument('id')

        query = "update ticket set response_ ='{}' where id_ = {}".format(body , id)
        self.db.execute(query)
        conn.commit()
        query = "update ticket set status_ = 0 where id_ = '{}'".format(id)
        self.db.execute(query)
        conn.commit()
        output = {"status" : "True"}
        self.write(output)
        

class changestatus(BaseHandler):

    def post(self , *args , **kwargs):
        api = self.get_argument('api')
        id = self.get_argument('id')
        status = self.get_argument('status')
        query = "update ticket set status_ = {0} where id_ = {1}".format(status , id)
        self.db.execute(query)
        conn.commit()
        output = {'status' : 'True'}
        self.write(output)
        
        

def main():
    clear()
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
