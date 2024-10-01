class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Name: {self.name} and Salary: {self.salary}")


emp1 = Employee("John", 1000)
emp1.show()
