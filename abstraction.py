class account:
    def __init__(self,name,balance=0,pin="0000"):
        self.name=name
        self.balance=balance
        self.__pin=pin #__ makes it private

    def checkbalance(self):
        return f"your balance is: {self.balance}"
    
    def deposit(self,ammount):
        self.balance+=ammount
        return f"{ammount} has been deposited succesfully your balance is now {self.balance}"
    
    def withdraw(self,take):
        if self.balance<take:
            return f"you have insifficent funds your current balance is {self.balance}"
        else:
            return f"{take} has been withdrawn succesfully your current balance is {self.balance-take}"
        
    def enter(self):
        num=input("please enter your pin: ")
        return self.__valadatepin(num)
    
    def __valadatepin(self,num):
        return num==self.__pin

holder1=account("bob",10000,"2468")

if holder1.enter():
    print("choose 1,2 or 3 \n1 is check balance \n2 is withdraw \n3 is deposite")
    choose=input("enter your choice: ")
    if choose=="1":
        print(holder1.checkbalance())
    elif choose=="2":
        amount=int(input("how much do you want to withdraw: "))
        print(holder1.withdraw(amount))
    elif choose=="3":
        money=int(input("how much would you like to deposit: "))
        print(holder1.deposit(money))
    else:
        print("invalid option")
else:
    print("that is incorrect please try again")