#Public
class Employee:
    def __init__(self,name,salary) -> None:
        self.name =  name
        self.__salary = salary

    def show(self):
        print(f"Your Name is {self.name} and Salary is {self.__salary}")


emp = Employee("Xyz","1230000")
emp.show() #>Only using method salary is accessible

print("--------------------------")
print(f"Your name is {emp.name} and Salary is {emp.salary}") #>> See, Attributes can not accessible from outside