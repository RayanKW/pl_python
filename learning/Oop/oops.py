from abc import ABC, abstractmethod
# dancing around with object oriented programming
class student:
    regNo = 4320
    name = 'wairimu'
    stream = '4f'
    def read (self):
        regNo= 123
        print("Read")
        print("rollNo is", regNo) # without self the p[riority is on the local variable i.e one created within the function
        print("rollNo is", self.regNo)#we use self to access the instance variable, i.e the ones created under the class.
    def write(self):
        print("writting")
a = student()
print("regNO", a.regNo)
print("name", student.name)
b = student()
print("stream", a.stream)
a.read()


            #>>>>single inheritance



class parent:
    def disply(self):
        print("I am parent")
class child(parent):
    def show(self):
        print ("I am child")
c1 = child()
c1.show()
c1.disply()#through inheritance the child also has parent's methods.


            #>>>>>multi level inheritance
            
            
# A child(derived class) inherits from the base class and that child acts as a parent to another child
class mainParent:
    def dis(self):
        print("I am the grandparet")
class prnt(mainParent):
    def sh(self):
        print("I am the derived class that acts as the base for the grandchild")
class grandChild(prnt):
    def hs(self):
        print("I am the grandchild")
gr = grandChild()
gr.dis()
gr.sh()
gr.hs()


            #>>>>>Heirachichal inheritance

#A base class can have multiple children.
class baseClass():
    def imsho(self):
        print("The base parent in heirachical")
class chil1(baseClass):
    def issho(self):
        print("I am child 2")
class child2(baseClass):
    def isho(self):
        print("I am child 2")
        #Note that the methods of child1 cannot and are not available to child2 and vice versa
ci = chil1()
ci.issho()
ci.imsho()
#but we can't have ci.isho() since child 2 does not inherit the methods of child 1 but only the base
#ci.isho() will result into an error

#>>>>Multiple inheritance

# -A derived class acquires or inherits from multiple base classes
class Father():
    def sho(self):
        print("I am one of the base class the derive class will inherit from")
class MOther():
    #encapsulation(wrapping of data and methods) >>private, public, protected
    name = "rayan" #public variable
    __name2 = "kiarie" #private scope
    def shw(self):# private method will be def __shw(self):
        print("I am also another base class the derived class will inherit from")
        print(self.__name2)#since name2 is of private scope it's only available in the class and cannot be accessed outside that class
class child(Father, MOther):
    def dis(self):
        print("I am the one inheriting")
a1 = child()
print(a1.name)
a1.sho()
a1.shw()
a1.dis()
#print(a1.__name2) >> this is what we mean. since __name2 is private its not accessible outside the class

"""Abstract  CLass and Abstract Methods
Abstract class only contains abstract methods. Abstract methods are methods with only declaration-
but not the definition.(recall abstract means hidding details)
Concerete class -- a class without abstract methods
Objects can only be instatiated in a concrete class and not in an abstract class """
#Abstact class
class aClass(ABC):
    @abstractmethod
    def display(self):
        None
    @abstractmethod
    def show(self):
        None
class ConcreteClass(aClass):
    def display(self):
        print("Abstract Method")
obj = ConcreteClass()
obj.display()
#The concrete class should implement all the abstract methods of the abstract class. if it fails then it is also an abstact class.