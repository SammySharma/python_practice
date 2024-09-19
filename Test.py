import random
from typing import List
class Bank():
    def __init__(self) -> None:
        self.account_holder_name:str = str(input("Please Enter Name: ")).title()
        self.account_type:str = str(input("Please Enter Account Type: ")).title()
        self.account_number:int = random.randrange(100000,999999)
        self.account_balance:float = 100.00

    
    def displayAllInfo(self):
        print("\n-----------------------")
        print(f"Account Number: {self.account_number}")
        print(f"Account Name: {self.account_holder_name}")
        print(f"Account Type: {self.account_type}")
        print(f"Account Balance: {self.account_balance}\n")
    
    def depositAmount(self,amount_deposit):
        if amount_deposit <= 0:
            print("You cannot add amount in Negative")
            return
        
        self.account_balance += amount_deposit
        print(f"Updated Balance is : {self.account_balance}")

    
    def withDrawAmount(self,amount_withdraw):
        if amount_withdraw > self.account_balance:
            print("Insufficient Amount")
            return
        
        self.account_balance -= amount_withdraw
        print(f"Amount {amount_withdraw} is withdrawl successfully.")
        print(f"Balance Amount is {self.account_balance}")

    def getBalance(self):
        print(f"Your account Balance is {self.account_balance}")



accounts:List[Bank]=[]
while True:
    print(
        """\n1. Add Account
2. Display all accounts
3. Search account
4. Get balance
5. Deposit 
6. Withdraw
7. Exit"""
    )
    choice = int(input("Enter your choice = "))
    match choice:
        case 1:
                obj=Bank()
                accounts.append(obj)
                print("Account Created!")
        case 2:
                for i in accounts:
                        i.displayAllInfo()
        case 3:

                acc_no:int = int(input("Please Enter Account Number: "))
                for i in accounts:
                    if i.account_number == acc_no:
                        i.displayAllInfo()
                        break
                    else:
                        print("Account Not Found")
        case 4:
                acc_no:int = int(input("Please Enter Account Number: "))
                for i in accounts:
                    if i.account_number == acc_no:
                        i.getBalance()
                        break
                    else:
                        print("Account Not Found")
        case 5:
                acc_no:int = int(input("Please Enter Account Number: "))
                deposit:float = float(input("Enter Amount to Deposit "))
                for i in accounts:
                    if i.account_number == acc_no:
                        i.depositAmount(deposit)
                        break
        case 6:
                acc_no:int = int(input("Please Enter Account Number: "))
                withdrawal:float = float(input("Enter Amount to Withdraw "))
                for i in accounts:
                    if i.account_number == acc_no:
                        i.withDrawAmount(withdrawal)
                        break
        
        case 7:

                break

        case _:
            if choice != range(1,8):
                    
                print("Invalid Choice")
        

        




