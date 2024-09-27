#Multilevel Inheritance
"""Single Inheritance """
class ABC:
    def func1(self):
        print("I am Func1 from class ABC")
    

class DEF(ABC):
    def func2(self):
        print("I am Func2 from Class DEF")

class XYZ(DEF):
    def func3(self):
        print("I am Func3 of class XYZ")


obj = XYZ()

#Calling Function 1 from Parent Class
obj.func1()

#Calling funtions 2 from 2nd Parent Class

obj.func2()

#calling function 3 from mu own class
obj.func3()


"""

"""
