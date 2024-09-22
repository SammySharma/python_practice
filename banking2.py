import random


class Bank:
    def __init__(self,holder_name:str,account_type:str) -> None: #Initializing the instance at the begining of Object
        self.account_holder_name = holder_name.title()
        self.account_number = random.randint(100000, 999999)
        self.balance = 100.0
        self.account_type = account_type.title()



    def __str__(self) -> str: #Dunder Method or Magic Method
        return f"{self.account_holder_name},Balance is : {self.balance}"
    
    
    def displayAllInfo(self):
        
        print("\n******Bank Account Information: *******")
        print(f"Account Holder's Name: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")
        print(f"Account Type: {self.account_type}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful.")
        print(f"New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful.")
            print(f"New Balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def getBalance(self):
        return self.balance


obj = Bank("John Doe","savings")
print(obj)

#obj.displayAllInfo()
