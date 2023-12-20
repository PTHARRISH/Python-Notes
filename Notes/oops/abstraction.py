# Abstraction:
# Abstraction is used to hide the internal functionality of the function from the users. 
# The users only interact with the basic implementation of the function, but inner working is hidden. 
# User is familiar with that "what function does" but they don't know "how it does."

# In simple words, we all use the smartphone and very much familiar with its functions such as camera,
# voice-recorder, call-dialing, etc., 
# but we don't know how these operations are happening in the background. 
# Let's take another example - When we use the TV remote to increase the volume. 
# We don't know how pressing a key increases the volume of the TV. 
# We only know to press the "+" button to increase the volume.

# Why Abstraction is Important?
# In Python, an abstraction is used to hide the irrelevant data/class in order to reduce the complexity. 
# It also enhances the application efficiency. 
# There are two types of abstraction. 
# One is data abstraction, wherein the original data entity is hidden via a data structure that can internally 
# work through the hidden data entities. 
# Other type is called process abstraction. 
# It refers to hiding the underlying implementation details of a process.
# Next, we will learn how we can achieve abstraction using the Python program.

# In object-oriented programming terminology, a class is said to be an abstract class if it cannot be instantiated, 
# that is you can have an object of an abstract class.
# You can however use it as a base or parent class for constructing other classes.

# To form an abstract class in Python, it must inherit ABC class that is defined in the abc module. 
# This module is available in Python's standard library. 
# Moreover, the class must have at least one abstract method. 
# Again, an abstract method is the one which cannot be called, but can be overridden. 
# You need to decorate it with @abstractmethod decorator.

# Abstraction classes in Python

# Abstract Base Classes
# An abstract base class is the common application program of the interface for a set of subclasses. 
# It can be used by the third-party, which will provide the implementations such as with plugins. 
# It is also beneficial when we work with the large code-base hard to remember all the classes.


# Working of the Abstract Classes
# Unlike the other high-level language, Python doesn't provide the abstract class itself. 
# We need to import the abc module, which provides the base for defining Abstract Base classes (ABC). 
# The ABC works by decorating methods of the base class as abstract. 
# It registers concrete classes as the implementation of the abstract base. 
# We use the @abstractmethod decorator to define an abstract method or if we don't provide the definition to the method, 
# it automatically becomes the abstract method. 
# Let's understand the following example.


# Example
from abc import ABC, abstractmethod
class demo(ABC):
    @abstractmethod
    def function1(self):
        print('this is abstract method')
        return
    
    def function2(self):
        print('this is concrete method')


# The demo class inherits ABC class. 
# There is function1() which is an abstract method. 
# Note that the class may have other non-abstract (concrete) methods.

# If you try to declare an object of demo class, Python raises TypeError −

# obj = demo() # TypeError: Can't instantiate abstract class demo with abstract method function1

# The demo class here may be used as parent for another class. However, the child class must override the abstract method in parent class. 
# If not, Python throws this error −TypeError: Can't instantiate abstract class concreteclass with abstract method method1
# Hence, the child class with the abstract method overridden is given in
print("-----------------------------Demo Example-----------------------------")
from abc import ABC,abstractmethod
class democlass(ABC):
    @abstractmethod
    def method1(self):
        print("this is abstract method")
        return
    
    def method2(self):
        print("this is concrete method")

class concreteclass(democlass):
    def method1(self):
        # democlass.method1(self)
        super().method1()
        return

obj=concreteclass()
obj.method1() # call the concrete class and override the base abstract class
obj.method2() # this is abstract method this is concrete method    


# Example -
print("-----------------------------Abstraction Car Class Example-----------------------------")
# Python program demonstrate  
# abstract base class work   
from abc import ABC, abstractmethod   
class Car(ABC):
    @abstractmethod    
    def mileage(self):   
        pass 
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")   
          
# Driver code   
t= Tesla ()   
t.mileage()   
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage() 



# Example for Abstract 
print("-----------------------------Abstraction Vehicle Class Example-----------------------------")
from abc import ABC, abstractmethod
class vehicle(ABC):
    def __init__(self,n):
        self.no_of_types=n
    
    @abstractmethod
    def start(self): 
        # same method name and same argument will passed in all the child class 
        # TypeError: scooty.start() takes 1 positional argument but 2 were given
        # every sub class are follow the rules
        # print("no start")
        pass

    def display(self):
        print("There are "+str(self.no_of_tyres)+" in the vehicle")

class scooty(vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.color=color
        self.no_of_tyres=n
    
    def start(self):
        super().start() # no start will display when you call abc method
        print('start with kicker')

class bike(vehicle):
    def __init__(self,n):
        super().__init__(n)
        self.no_of_tyres=n
    
    def start(self):
        print('self start')

class car(vehicle):
    def __init__(self,n,gears):
        super().__init__(n)
        self.gears=gears
        self.no_of_tyres=n
    
    def start(self):
        print('start with key')

scooty=scooty(2,'blue')
scooty.start()
scooty.display()

bike=bike(2)
bike.start()
bike.display()

car=car(4,6)
car.start()
car.display()

print("-------------------------------------------------------------------------------------------")