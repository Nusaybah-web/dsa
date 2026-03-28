class password:
    def __init__(self,pin="0000"):
        self.pin=pin
    def change(self):
        oldpass=input("please enter your password ")
        if self.pin==oldpass:
            newpass=input("plase eneter your new password ")
            self.pin=newpass
            print("your password has been succesfully updated ")
        else:
            print("that is the incorrect password")
            
changepass=password()
changepass.change()