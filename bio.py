import csv
class Detail:
    def __init__(self):
        print("\n")
    def myprofile(self):
        print("------MYPROFILE-----------")
        import login 
        lname = login.loginname
        lpsswd = login.loginpassword
        with open('data.csv','r')as file:
            f = csv.reader(file)
            for lines in file:
                data=lines.split(",")
                if(data[0]==lname and data[1]==lpsswd):
                    print("Email Id: ",data[2])
                    print("Name: ",data[0])
                    print("City: ",data[3])
                    print("Password: ",data[1])
        file.close()
        print("1.Home\t2.MyCourses\t3.Logout")
        ch = int(input())
        if(ch==1):
            from home_page import Home
            h=Home()
            h.home()
        elif(ch==2):
            from Mycourse import courses
            course=courses()
            course.mycourses()
        elif(ch==3):
            from logout import Logout
            lo = Logout()
            lo.logout()  
        else:
            print("Invalid number")
det = Detail()
#det.myprofile()