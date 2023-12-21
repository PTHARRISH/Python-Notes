# Python - Encapsulation
# Encapsulation is one of the key concepts of object-oriented languages like Python, Java, etc. 
# Encapsulation is used to restrict access to methods and variables. 
# In encapsulation, code and data are wrapped together within a single unit from being modified by accident.
# Encapsulation is a mechanism of wrapping the data (variables) and code acting on the data (methods) together as a single unit.
# In encapsulation, the variables of a class will be hidden from other classes, 
# and can be accessed only through the methods of their current class.


# Real-World Example:
# Lets Take a look at a real-world example of encapsulation. 
# There are many sections in a company, such as the accounts and finance sections. 
# The finance section manages all financial transactions and keeps track of all data. 
# The sales section also handles all sales-related activities. 
# They keep records of all sales. 
# Sometimes, a finance official may need all sales data for a specific month. 
# In this instance, he is not permitted to access the data from the sales section. 
# First, he will need to contact another officer from the sales section to request the data. This is encapsulation. 
# The data for the sales section, as well as the employees who can manipulate it, 
# are all wrapped together under the single name "sales section". 
# Encapsulation is another way to hide data. 
# This example shows that the data for sections such as sales, finance, and accounts are hidden from all other sections.


# Python encapsulation example
# The following defines the Counter class:

print("----------------------------------Public Members------------------------------------")

class Counter:
    def __init__(self):
        self.current=0
    
    def increment(self):
        self.current+=1

    def value(self):
        return self.current
    
    def reset(self):
        self.current=0


# The Counter class has one attribute called current which defaults to zero. And it has three methods:

# increment() increases the value of the current attribute by one.
# value() returns the current value of the current attribute
# reset() sets the value of the current attribute to zero.
# The following creates a new instance of the Counter class and calls the increment() method three times 
# before showing the current value of the counter to the screen:

counter = Counter()
counter.increment() # 1
counter.increment() # 2
counter.increment() # 3
print("Current value of the Counter class: ",counter.value()) # 3

# It works perfectly fine but has one issue.

# From the outside of the Counter class, you still can access the current attribute and change it to whatever you want. 
# For example:
counter = Counter()
counter.increment() # 1
counter.increment() # 2
counter.current = -3
print("Current value modified by outside the Counter class: ",counter.value()) # -3

# In this example, we create an instance of the Counter class, 
# call the increment() method twice and set the value of the current attribute to an invalid value -3.
# So how do you prevent the current attribute from modifying outside of the Counter class?
# That’s why private attributes come into play.

print("-------------------------------Protected Members------------------------------------")

# Protected Members
# Protected members in C++ and Java are members of a class that can only be accessed within the class 
# but cannot be accessed by anyone outside it. 
# This can be done in Python by following the convention and prefixing the name with a single underscore.

# The protected variable can be accessed from the class and in the derived classes 
# (it can also be modified in the derived classes), but it is customary to not access it out of the class body.
# The __init__ method, which is a constructor, runs when an object of a type is instantiated.

# Python program for demonstrating protected members  
  
# first, we will create the base class  
class Base1:  
    def __init__(self):  
        # the protected member variable  
        self._p = 78  
  
# Here, we will create the derived class  
class Derived1(Base1):  
    def __init__(self):  
        # Now, we will call the constructor of Base class  
        Base1.__init__(self)  
        print ("We will call the protected member of base class: ", self._p)  
  
        # Now, we will be modifing the protected variable:  
        self._p = 433  
        print ("we will call the modified protected member outside the class: ", self._p)  
  
  
obj1 = Derived1()  
obj2 = Base1()  
  
# Here, we will call the protected member  
print ("Access the protected member of obj1: ", obj1._p)  
# Here, we will access the protected variable outside  
print ("Access the protected member of obj2: ", obj2._p)  
# To modify the protected variable program visit the access_modifier.py file


print("-------------------------Private Members using name mangling--------------------------")
# Private attributes
# Private members are the same as protected members. 
# The difference is that class members who have been declared private 
# should not be accessed by anyone outside the class or any base classes. 
# Python does not have Private instance variable variables that can be accessed outside of a class.
# However, to define a private member, prefix the member's name with a double underscore "__".


# Example for Student:
# Let us create the Student class.Make name private and marks as private by prefixing double underscores to them.

class Student:

   def __init__(self, name="Harrish", marks=50):
      self.__name = name
      self.__marks = marks
   def studentdata(self):
      print ("Name: {} marks: {}".format(self.__name, self.__marks))
      
s1 = Student()
s2 = Student("Harri", 25)

s1.studentdata()
s2.studentdata()
# print ("Name: {} marks: {}".format(s1.__name, s2.__marks))
# print ("Name: {} marks: {}".format(s2.__name, __s2.marks))

# output:
# When you run this code, it will produce the following output −
# Name: Harrish marks: 50
# Name: Harri marks: 25
# Traceback (most recent call last):
#  File "C:\Python311\hello.py", line 14, in <module>
#   print ("Name: {} marks: {}".format(s1.__name, s2.__marks))
# AttributeError: 'Student' object has no attribute '__name'

# The above output makes it clear that the instance variables name and marks, 
# although they can be accessed by a method declared inside the class (the studentdata() method), 
# but since the double underscores prefix makes the variables private, 
# and hence accessing them outside the class is disallowed, raising Attribute error.
# Python doesn't block access to private data entirely. 

# You can still access the private members by Python's name mangling technique.

# Name mangling is the process of changing name of a member with double underscore to the form 
# object._class__variable. 
# If so required, it can still be accessed from outside the class, but the practice should be refrained.
# In our example, the private instance variable "__name" is mangled by changing it to the format


# So, to access the value of "__marks" instance variable of "s1" object, change it to "s1._Student__marks".
# Change the print() statement in the above program to −
print ("Before modifying private variable s1.mark: ",s1._Student__marks)
# It now prints 50, the marks of s1.
s1._Student__marks=100 # you can change the private using name mangling
print ("After modifying private variable s1.mark : ",s1._Student__marks) 


print("------------------------Private Members using setter function-------------------------")
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    # setter function to modify the private variable
    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell() # 900

# change the price
c.__maxprice = 1000
# print(c.__maxprice) # print outside class values only
c.sell() # 900

# using setter function
c.setMaxPrice(1000)
c.sell() # 1000

# In the above program, we defined a Computer class.
# We used __init__() method to store the maximum selling price of Computer. Here, notice the code
# c.__maxprice = 1000
# Here, we have tried to modify the value of __maxprice outside of the class. 
# because the variable shown the c.__maxprice=1000 outside the class only
# However, since __maxprice is a private variable, this modification is not seen on the output.
# As shown, to change the value, we have to use a setter function 
# i.e setMaxPrice() which takes price as a parameter.