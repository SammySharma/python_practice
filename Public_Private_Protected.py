#Public
class Employee:
    def __init__(self,name,salary) -> None:
        self.name =  name
        self.salary = salary

    def show(self):
        print(f"Your Name is {self.name} and Salary is {self.salary}")


emp = Employee("Xyz","1230000")
emp.show()

print("--------------------------")
print(f"Your name is {emp.name} and Salary is {emp.salary}") #>> See, Attributes are accessible from outside