class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        print("Getter Methdo Called")
        return self.__age

    @age.setter
    def age(self, new_age):
        print("Setter Method Called")
        self.__age = new_age


obj1 = Student("Ram", 25)
print(obj1.age)
print("-----------------")
obj1.age = 26
print(obj1.age)

""" Getter and Setter methods used when we need to change the value of private variable outside of the class"""
