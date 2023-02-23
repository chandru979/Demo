class main:
    def choose(self):
        print("\t\t------KNOWLEDGE BASE - LEARNING PORTAL-------\n")
        print("1.REGISTER \n2.USER LOGIN\n3.ADMIN LOGIN")
        log = int(input())
        if(log == 1):
            from Validate import validate
            val=validate()
            val.Register()
        elif(log == 2):
            from login import Login
            log = Login()
            log.login()
        elif(log ==3):
            from Admin_login import Admin
            ad = Admin()
            ad.adlogin()

m = main()
m.choose()