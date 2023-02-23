class Admin:
    def __init__(self):
        self.admin_name = "chan"
        self.admin_password = "chan@123"
    def adlogin(self):
        self.name = input("Admin name: ")
        self.psswd = input("password: ")
        if(self.admin_name == self.name and self.admin_password == self.psswd):
            f=open("data.csv","r")
            print(f.read())
            print("1.Add user\t2.Logout")
            ch = int(input())
            if(ch==1):
                from Validate import validate
                val=validate()
                val.Register()
            elif(ch==2):
                exit()
        else:
            print("Invalid admin name or password")
            ad.adlogin()
    
ad = Admin()
