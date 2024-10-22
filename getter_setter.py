class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # Getter Method
    def get_age(self):
        return self.__age

    # Setter Method
    def set_age(self, new_age):
        self.__age = new_age


s1 = Student("John", 21)
print(s1.name)
print("-----------------")
print(s1.get_age())
print("-----------------")
s1.set_age(23)
print(s1.get_age())
