class courses:
    def __init__(self):
        pass
    def mycourses(self):
        print("\n1.Python\t2.Java\t3.RDBMS\t4.Home")
        ch = int(input())
        if(ch==1):
            course.python()  
        elif(ch==2):
            course.java()
        elif(ch==3):
            course.rdbms() 
        elif(ch==4):
            course.home()
        else:
            print("Invalid number")
            course.mycourses()
    def python(self):
        try:
            f=open("python_course.txt","r")
            print(f.read())
            #print(f.closed)
            course.mycourses()
            
        except:
            pass
        finally:
            f.close()
        
    def java(self):
        try:
            f=open("java.txt","r")
            print(f.read())
            course.mycourses()
            
        except:
            pass
        finally:
            f.close()
            
            
    def rdbms(self):
        try:
             f=open("rdbms_course.txt","r")
             print(f.read())
             course.mycourses()
             
        except:
            pass
        finally:
            f.close()
             
    def home(self):
        from home_page import Home
        h=Home()
        h.home()

course = courses()
#course.mycourses()