class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.__salary = salary

    def show(self):
        print(f"Name: {self.name} and Salary: {self.__salary}")


emp1 = Employee("John", 1000)
emp1.show()
"""Since Salary became private, we can't access it from outside the class
That is why we get error when we run code line number 14"""
print(emp1.__salary)
