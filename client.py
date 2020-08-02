import requests
import os 
import time 
import platform 
import sys 
from gtts import gTTS
import pyttsx3



PARAMS = CMD = USERNAME = PASSWORD = API = ""
HOST = '127.0.0.1'
PORT = '1104'

def __postcr__():
    return "http://" + HOST + ":" + PORT + "/" + CMD + "?"

def __api__():
    return "http://" + HOST + ":" + PORT + "/" + CMD + "/" + API

def __authgetcr__():
    return "http://"+HOST+":"+PORT+"/"+CMD

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

ADDRESS = "http://127.0.0.1:1104/"

def pr():
    print("""
    --------------------------------------------------------------------------------
    --                                                                            --
    --                                                                            --
    --                                                                            --
    --                                                                            --
    --                                                                            --
    --                    wellcome to ticket management system                    --
    --                                                                            --
    --                     Designed and Created by : @pr.1266                     --
    --                                                                            --
    --                                                                            --
    --                                                                            --
    --                                                                            --
    --                                                                            --
    --                                                                            --
    --                                                                            --
    --                                                                            --
    --                                                                            --
    --                                                                            --
    --                                                                            --
    --                                                                            --
    --------------------------------------------------------------------------------
    
    """)
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)    # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1
    engine.say('wellcome to ticket management system')
    engine.say('it designed by poorya')
    engine.runAndWait()


def start():
    print("""please choose the command that you want to do :
    1 . signup
    2 . login
    3 . exit
    """)


def signup_menu():
    print("please enter your username and password to signup :")
    print("USERNAME : ")
    username = sys.stdin.readline()[:-1]
    print("PASSWORD : ")
    password = sys.stdin.readline()[:-1]
    return username , password

def login_menu():
    print("please enter your username and password to login :")
    print("USERNAME : ")
    username = sys.stdin.readline()[:-1]
    print("PASSWORD : ")
    password = sys.stdin.readline()[:-1]
    return username , password
    
def client_menu():
    #print("USERNAME : {}\nAPI : {}".format(USERNAME , API))
    print("""what do you prefer to do ?
    1 . send tickets
    2 . get ticket
    3 . close a ticket
    4 . logout
    5 . exit
    """)

def admin_menu():
    #print("USERNAME : "+USERNAME+"\n"+"API : " + API)
    print("""What Do You Prefer To Do ?
    1 . get ticket
    2 . response to ticket
    3 . change status of a ticket
    4 . logout
    5 . exit
    """)

def run():
    clear()
    pr()
    time.sleep(2)
    while True:
        clear()
        start()
        status = sys.stdin.readline()[:-1]
        if status == '1': #status == sign up
            clear()
            USERNAME , PASSWORD = signup_menu()
            CMD = "signup"
            q = ADDRESS + CMD
            print(q)
            PARAMS = {'username' : USERNAME , "password" : PASSWORD}
            data = requests.post(url = q , data = PARAMS)
            r = data.json()
            print(r)
            if str(r['status']) == 'True':
                clear()
                print("Sign up completed !")
                time.sleep(2)
            else:
                print("Sign up failed !")
                time.sleep(2)
        elif status == '2': #status == login
            clear()
            USERNAME , PASSWORD = login_menu()
            CMD = "login"
            q = ADDRESS + CMD
            PARAMS = {'username' : USERNAME , 'password' : PASSWORD} 
            r = requests.post(q , params = PARAMS)
            r = r.json()
            print(r)
            if str(r['status']) == 'True':
                clear()
                print("USERNAME and PASSWORD are Correct\nLogging you in ...")
                API = r['api']
                ROLE = r['role']
                time.sleep(2)
                while True:
                    if ROLE == 0: #client
                        clear()
                        print("Username : {} , Api : {}".format(USERNAME , API))
                        client_menu()
                        status = sys.stdin.readline()[:-1]
                        if status == '1':
                            CMD = 'sendticket'
                            print("please enter the subject of Ticket ...")
                            subject = sys.stdin.readline()[:-1]
                            print("now please enter the Body of Ticket ...")
                            body = sys.stdin.readline()[:-1]
                            PARAMS = {"subject" : subject , "body" : body , "api" : API}
                            q = ADDRESS + CMD
                            r = requests.post(q , PARAMS).json()
                            if str(r['status']) == 'True':
                                print("ticket send successfully")
                                time.sleep(2)
                        elif status == '2':
                            clear()
                            CMD = 'getticketcli'
                            q = ADDRESS + CMD
                            PARAMS = {"api" : API}
                            r = requests.post(q , PARAMS).json() 
                            
                            
                            my_list2 = []
                            #for i in range(len(r['response'])):
                            #    print(r['response'][i])                                
                            #print(r['response'][0])
                            for i in range(len(r['response'])):
                                my_list1 = []
                                my_list1.append(r['response'][i][0])
                                my_list1.append(r['response'][i][1])
                                my_list1.append(r['response'][i][2])
                                my_list1.append(r['response'][i][3])
                                my_list1.append(r['response'][i][4])
                                my_list1.append(r['response'][i][5])
                                my_list2.append(my_list1)
                                del my_list1
                            for i in my_list2:
                                print("id = {}".format(i[0]))
                                print("sender = {}".format(i[1]))
                                print("subject = {}".format(i[3]))
                                print("body = {}".format(i[2]))
                                print("response : {}".format(i[5]))
                                if i[4] == 0:
                                    print("status : Close")
                                elif i[4] == 1:
                                    print("status : Open")
                                else:
                                    print("status : in queue")
                                print("\n")

                            #print(my_list2)
                            time.sleep(2)
                            print("press any key to continue")
                            x = sys.stdin.readline()

                        elif status == '3':
                            clear()
                            CMD = 'getticketcli'
                            q = ADDRESS + CMD
                            PARAMS = {"api" : API}
                            r = requests.post(q , PARAMS).json() 
                            
                            
                            my_list2 = []
                            #for i in range(len(r['response'])):
                            #    print(r['response'][i])                                
                            #print(r['response'][0])
                            for i in range(len(r['response'])):
                                my_list1 = []
                                my_list1.append(r['response'][i][0])
                                my_list1.append(r['response'][i][1])
                                my_list1.append(r['response'][i][2])
                                my_list1.append(r['response'][i][3])
                                my_list1.append(r['response'][i][4])
                                my_list1.append(r['response'][i][5])
                                my_list2.append(my_list1)
                                del my_list1
                            for i in my_list2:
                                print("id = {}".format(i[0]))
                                print("sender = {}".format(i[1]))
                                print("subject = {}".format(i[3]))
                                print("body = {}".format(i[2]))
                                print("response : {}".format(i[5]))
                                if i[4] == 0:
                                    print("status : Close")
                                elif i[4] == 1:
                                    print("status : Open")
                                else:
                                    print("status : in queue")
                                print("\n")
                            
                            print("please select a open ticket to close :")
                            id_ = sys.stdin.readline()[:-1]
                            CMD = 'closeticket'
                            q = ADDRESS + CMD
                            PARAMS = {'id' : id_ , 'api' : API}
                            r = requests.post(q , PARAMS).json()
                            if str(r["status"]) == "True":
                                print("ticket successfuly closed")
                                time.sleep(2)
                            
                        elif status == '4':
                            clear()
                            #CMD = "logout"
                            #PARAMS = {'username' : USERNAME , 'password' : PASSWORD}
                            #q = ADDRESS + CMD
                            #r = requests.post(query , params = PARAMS).json()
                            #if r['status']:
                            USERNAME = PASSWORD = CMD = API = ""
                            print("loged out successfully")
                            time.sleep(3)
                            break
                            
                        elif status == '5':
                            print("good bye !")
                            time.sleep(3)
                            sys.exit()
                    else: #admin
                        clear()
                        admin_menu()
                        status = sys.stdin.readline()[:-1]
                        if status == '1':
                            CMD = 'getticketmod'
                            q = ADDRESS + CMD
                            PARAMS = {"api" : API}
                            r = requests.post(q , PARAMS).json()
                            my_list2 = []
                            #for i in range(len(r['response'])):
                            #    print(r['response'][i])                                
                            #print(r['response'][0])
                            for i in range(len(r['response'])):
                                my_list1 = []
                                my_list1.append(r['response'][i][0])
                                my_list1.append(r['response'][i][1])
                                my_list1.append(r['response'][i][2])
                                my_list1.append(r['response'][i][3])
                                my_list1.append(r['response'][i][4])
                                my_list1.append(r['response'][i][5])
                                my_list2.append(my_list1)
                                del my_list1
                            for i in my_list2:
                                print("id = {}".format(i[0]))
                                print("sender = {}".format(i[1]))
                                print("subject = {}".format(i[3]))
                                print("body = {}".format(i[2]))
                                print("response : {}".format(i[5]))
                                if i[4] == 0:
                                    print("status : Close")
                                elif i[4] == 1:
                                    print("status : Open")
                                else:
                                    print("status : in queue")
                                print("\n")
                            print("press any key to continue ...")
                            x = sys.stdin.readline()[:-1]
                            
                        elif status == '2':

                            CMD = 'getticketmod'
                            q = ADDRESS + CMD
                            PARAMS = {"api" : API}
                            r = requests.post(q , PARAMS).json()
                            my_list2 = []
                            #for i in range(len(r['response'])):
                            #    print(r['response'][i])                                
                            #print(r['response'][0])
                            for i in range(len(r['response'])):
                                my_list1 = []
                                my_list1.append(r['response'][i][0])
                                my_list1.append(r['response'][i][1])
                                my_list1.append(r['response'][i][2])
                                my_list1.append(r['response'][i][3])
                                my_list1.append(r['response'][i][4])
                                my_list1.append(r['response'][i][5])
                                my_list2.append(my_list1)
                                del my_list1
                            for i in my_list2:
                                print("id = {}".format(i[0]))
                                print("sender = {}".format(i[1]))
                                print("subject = {}".format(i[3]))
                                print("body = {}".format(i[2]))
                                print("response : {}".format(i[5]))
                                if i[4] == 0:
                                    print("status : Close")
                                elif i[4] == 1:
                                    print("status : Open")
                                else:
                                    print("status : in queue")
                                print("\n")

                            print("please enter the id of ticket that you want to response :")
                            id_ = sys.stdin.readline()[:-1]
                            print("please enter the response :")
                            body = sys.stdin.readline()[:-1]
                            PARAMS = {"body" : body , "api" : API , "id" : id_}
                            CMD = 'restoticketmod'
                            q = ADDRESS + CMD
                            r = requests.post(q , PARAMS).json()
                            if str(r['status']) == 'True':
                                print("response successfully submited and ticket closed")
                                time.sleep(2)
                            else:
                                print("some errors happend !")

                        elif status == '3':
                            CMD = 'getticketmod'
                            q = ADDRESS + CMD
                            PARAMS = {"api" : API}
                            r = requests.post(q , PARAMS).json()
                            my_list2 = []
                            #for i in range(len(r['response'])):
                            #    print(r['response'][i])                                
                            #print(r['response'][0])
                            for i in range(len(r['response'])):
                                my_list1 = []
                                my_list1.append(r['response'][i][0])
                                my_list1.append(r['response'][i][1])
                                my_list1.append(r['response'][i][2])
                                my_list1.append(r['response'][i][3])
                                my_list1.append(r['response'][i][4])
                                my_list1.append(r['response'][i][5])
                                my_list2.append(my_list1)
                                del my_list1
                            for i in my_list2:
                                print("id = {}".format(i[0]))
                                print("sender = {}".format(i[1]))
                                print("subject = {}".format(i[3]))
                                print("body = {}".format(i[2]))
                                print("response : {}".format(i[5]))
                                if i[4] == 0:
                                    print("status : Close")
                                elif i[4] == 1:
                                    print("status : Open")
                                else:
                                    print("status : in queue")
                                print("\n")

                            print("select id of ticket too change status :")
                            print("ID : ")
                            id_ = sys.stdin.readline()[:-1]
                            print("STATUS : ")
                            print("""
                            1 . to close enter 0
                            2 . to open enter 1
                            3 . to in queue enter 2
                            """)
                            status_ = sys.stdin.readline()[:-1]
                            PARAMS = {"id" : id_ , "status" : status_ , "api" : API}
                            CMD = "changestatus"
                            q = ADDRESS + CMD
                            r = requests.post(q , params = PARAMS).json()
                            if str(r['status']) == 'True':
                                print("status changed successfully")
                                time.sleep(2)
                            else:
                                print("some errors happend !")
                                time.sleep(2)

                        elif status == '4':
                            USERNAME = PASSWORD = CMD = API = ""
                            print("loged out successfully")
                            time.sleep(3)
                            break
                        elif status == '5':
                            sys.exit()    

            else:
                print("InCorrect USERNAME and PASSWORD")
                time.sleep(2)
            #hala ke login kard baadesh menu aslie miad :
        elif status == '3': #status == exit 
            clear()
            sys.exit()
        else:
            print("Wrong command you choose please try again")
        
if __name__ == "__main__":

    run()