# Encapsulation (Public,Private,Protected (access modifiers))
class Person:
    def __init__(self) -> None:
        # Data Members
        self.first_name = input("Enter First Name: ")
        self.last_name = input("Enter Last Name: ")
        self.phone_number = int(input("Enter Phone Number : "))

    def displayDetails(self):
        print(f"My First name is {self.first_name}")
        print(f"My Last name is {self.last_name}")
        print(f"My Phone number is  {self.phone_number}")


obj = Person()
obj.first_name = "Test"  # This is publicly accessible
obj.displayDetails()


"""
1. Public -> Accessible anywhere outside from class
2. Private -> Accessible within the class 
3. Protected -> Accessible within the class and its subclass
"""
