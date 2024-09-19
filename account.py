from decimal import Decimal
class Account:


    def __init__(self,name,balance):
        if balance < Decimal ('0.00'):
            raise ValueError("Initial Balance can not be 0.00")
        
        self.name = name
        self.balance = balance
    
    def deposit(self,amount):
        if amount < Decimal('0.00'):
            raise ValueError("Amount must be positive")
        
        self.balance += amount

    def withdrawl(self,amount):
        if amount > self.balance:
            raise ValueError(" You can not withdraw the Amount More than the Balance")
        elif amount < Decimal('0.00'):
            raise ValueError("Amount can not be 0.00 or Negative")
        
        self.balance -= amount



