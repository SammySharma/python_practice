"""Private_&_Protected"""
class Company:
    def __init__(self) -> None:
        self._project = "Gen AI & Computer Vison"
        print("I am Constructor of Company")
    


class Employee(Company):
    def __init__(self,name) -> None:
        self.name = name
        print("I am Constructor of Employee")
        super().__init__()


obj = Employee("John")

print(obj._project) #Accessing Protected object with use of Inheritance

"""
In Above example, you can see that "self._project" is part of company and it is a protected attribute.
If i call objected are comment line 13 then i will only get "I am constructor of Employee" but you can clearly
see that after using super function we are accessing attributes of Company and assigning those to Employee Class.
Even though We did not set project of Employee , yet it adapts the values from its parent class.
"""