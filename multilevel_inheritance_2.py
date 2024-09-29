#Multilevel Inheritance
"""Single Inheritance """
class ABC:
    def func(self):
        print("I am Func1 from class ABC")
    

class DEF(ABC):
    def func(self):
        print("I am Func2 from Class DEF")

        

class XYZ(DEF):
    def func3(self):
        print("I am Func3 of class XYZ")
        ABC_Func = super().func()
        print(f"Original Function from ABC {ABC_Func}")


obj = XYZ()

#Accessing Object from Another class which have same name

obj.func()
