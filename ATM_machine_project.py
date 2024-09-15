class ATM:
    def __init__(self,balance=0,pin=0000):
        self.balance=balance
        self.pin=pin
    def Check_balance(self):
        self.balance
        return self.balance
    def Deposit(self,amount):
        old_balance=self.balance
        self.balance+=amount
        return f"Deposit successfull.Before Deposit {old_balance} current balance {self.balance}"
    def after_deposit(self):
        return self.balance
    def Withdraw(self,amount):
        if amount>self.balance:
            return "insuficient Money"
        else:
            old_balance=self.balance
            self.balance-=amount
            return f"withdraw successfull.Before Withdraw {old_balance} current balance {self.balance}"
    def after_withdraw(self):
        return self.balance
    def Change_pin(self,new_pin):
        self.pin=new_pin
        return "Pin Changed Successfully"
    def after_change_pin(self):
        return self.pin
def main():
    atm=ATM(1000,2024)
    count=1
    try_again=0

    while count>try_again:
        if count==6:
            print("You are Invalid Person")
            break
              
        print("________Welcome to the Atm machine.________\n")
        pin=int(input("Please Enter Your Pin :")) 

        if pin!=atm.pin:            
            print("Encorrect Pin.Please Try Again..")
            count+=1                       
            continue

        print("\nEnter 1 for check balance\nEnter 2 for Deposit\nEnter 3 for withdraw\nEnter 4 for change pin\nEnter 5 for Exit")
        opt = int(input("\nEnter your choice :"))

        if(opt>5 or opt<=0):       
            print("Invalid option.Please Try Again..")

        if opt==5:
            print("Thanks for using the ATM")
            try_again=2
            break
      
        while(opt==1 or opt==2 or opt==3 or opt==4 or opt==5):      
            if opt==1:
                print("Your Current Balance",atm.Check_balance())
                print("______________________________")
                import json
                balance=atm.Check_balance()
                f=open("ATM.txt","a")
                data={"Current Balance":balance}
                json.dump(data,f)
                f.write("\n")
                f.close()          
            elif opt==2:
                amount=float(input("Enter Amount For Deposit :"))
                print(atm.Deposit(amount))
                import json
                deposit=atm.after_deposit()
                f=open("ATM.txt","a")
                data={"After Deposit Balance":deposit}
                json.dump(data,f)
                print("______________________________")
                f.write("\n")
                f.close()
            elif opt==3:
                amount=float(input("Enter Amount For Withdraw :"))
                print(atm.Withdraw(amount))
                import json
                withdraw=atm.after_withdraw()
                f=open("ATM.txt","a")
                data={"After withdraw Balance":withdraw}
                json.dump(data,f)
                print("______________________________")
                f.write("\n")
                f.close()
            elif opt==4:
                pin=int(input("Enter Your New Pin :"))
                print(atm.Change_pin(pin))
                import json
                change_pin=atm.after_change_pin()
                f=open("ATM.txt","a")
                data={"After change pin":change_pin}
                json.dump(data,f)
                print("______________________________")
                f.write("\n")
                f.close()
            elif opt==5:
                print("Thanks for using the ATM")
                try_again=2
                break

            print("Enter 1 for check balance\nEnter 2 for Deposit\nEnter 3 for withdraw\nEnter 4 for change pin\nEnter 5 for Exit")
            opt = int(input("\nEnter your choice :"))     
main()