import csv
import re
class validate:
     def Register(self):
        print("----------REGISTER-------------")
        
        flag = True
        while(flag):
            data = []
            global newname,newemailid,newconfirmpassword,newcity,newpassword
            newname = input("Name: ")
            data.append(newname)
            flag1 = True
            while(flag1):
                 print("password should contains 1-uppercase,1-lowercase,1-special symbol")
                 newpassword = input("password: ")
                 if re.match(r'[A-Za-z0-9@#$]{6,12}', newpassword):
                    data.append(newpassword)
                    l=len(newpassword)
                    if(l<7):
                        print("weak password")
                    else:
                        print("strong password")
                    flag1 = False
                 else:
                    print("Invalid password")
            flag2=True
            while(flag2):
                 newemailid = input("Email_Id: ")
                 if re.match(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', newemailid):
                     data.append(newemailid)
                     flag2 = False
                 else:
                     print("Invalid email")
            newcity = input("City/Town: ") 
            data.append(newcity)
            newconfirmpassword = input("Confirm Password: ")
            data.append(newconfirmpassword)
            print("\n")
            if(newpassword != newconfirmpassword):
                print("Incorrect password")
                flag = True
            else:
                print("Register Successfully...")
                with open('data.csv','a',newline='')as file:
                    f = csv.writer(file)
                    f.writerow(data)
                file.close()
                from login import Login
                log = Login()
                log.login()
                
val = validate()


