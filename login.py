import csv
class Login:
    def __init__(self):
        print("\n")
    def login(self):
        global loginname,loginpassword
        print("\t\t-----------LOGIN-----------") 
        flag = True
        while flag:
            loginname = input("UserName: ")
            loginpassword = input("Password: ") 
            with open('data.csv','r')as file:
                f=csv.reader(file)
                # row = file.readlines()
                for lines in file:
                    data=lines.split(",")
                    #print(data)
                    #print(data[0],loginname)
                    #try:
                    if(data[0] == loginname and data[1] == loginpassword):
                        print("login successfully...")
            file.close()
            flag = False
        from home_page import Home
        h=Home()
        h.home()
                                

log = Login()
#log.login()