"""Single Inheritance """
class ABC:
    def func1(self):
        print("I am Func1 from class ABC")
    

class DEF(ABC):
    def func2(self):
        print("I am Func2 from Class DEF")


obj = DEF()

#Calling Function 1 from Parent Class
obj.func1()

#Calling my own function , func2 from my own class

obj.func2()


"""

"""
