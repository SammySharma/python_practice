"""If you dumping class in a pickle object, class code must be available otherwise it wont work"""

import pickle


class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


s = Student("John", 25)
with open("student.data", "wb") as f:
    pickle.dump(s, f)


with open("student.data", "rb") as f:
    data = pickle.load(f)
    print(data.name)
    print(data.age)
    data.display()
