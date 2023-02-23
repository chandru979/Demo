
class Home:
    def __init__(self):
        pass
    def home(self):
        f=open('home.txt','r')
        print(f.read())
        print("\n\n")
        f.close()
        h.choose()
        
    def choose(self):
        print("\n1.Profile\t2.MyCourses")
        ch = int(input())
        if(ch==1):
            from bio import Detail
            d=Detail()
            d.myprofile()
        elif(ch==2):       
            from Mycourse import courses    
            cour=courses()
            cour.mycourses()
        else:
            print("Invalid input")
   
h = Home()
#h.home()
