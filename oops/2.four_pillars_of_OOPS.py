# Python Inheritance
# Inheritance is the capability of one class to derive or inherit the properties from another class. 
# The class that derives properties is called the derived class or child class and the class from 
# which the properties are being derived is called the base class or parent class. 
# The benefits of inheritance are:

# It represents real-world relationships well.
# It provides the reusability of a code. 
# We don’t have to write the same code again and again. 
# Also, it allows us to add more features to a class without modifying it.
# It is transitive in nature, which means that if class B inherits from another class A, 
# then all the subclasses of B would automatically inherit from class A.


# Types of Inheritance

# Single Inheritance: 
# Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.

# Multilevel Inheritance: 
# Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from his parent class. 

# Hierarchical Inheritance: 
# Hierarchical-level inheritance enables more than one derived class to inherit properties from a parent class.

# Multiple Inheritance: 
# Multiple-level inheritance enables one derived class to inherit properties from more than one base class.


# Inheritance in Python

# Python code to demonstrate how parent constructors
# are called.
print("__________________________________________________________")
print("Inheritance class in Python")
print("__________________________________________________________")
# parent class
class Person(object):

	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)
		
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
	
# child class
class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		Person.__init__(self, name, idnumber)
		
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
		print("Post: {}".format(self.post))


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
a.display()
a.details()


# we have created two classes 
# i.e. Person (parent class) and Employee (Child Class). 
# The Employee class inherits from the Person class. 
# We can use the methods of the person class through the employee class as seen in the display function in the above code. 
# A child class can also modify the behavior of the parent class as seen through the details() method.


# Python Polymorphism
# Polymorphism simply means having many forms. 
# For example, we need to determine if the given species of birds fly or not, 
# using polymorphism we can do this using a single function.

# Polymorphism in Python

print("__________________________________________________________")
print("Polymorphism and Inheritance class in Python")
print("__________________________________________________________")
class Bird:

	def intro(self):
		print("There are many types of birds.")

	def flight(self):
		print("Most of the birds can fly but some cannot.")

class sparrow(Bird):

	def flight(self):
		print("Sparrows can fly.")

class ostrich(Bird):

	def flight(self):
		print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro() # call and print the parent class function
obj_spr.flight()

obj_ost.intro() # call and print the parent class function
obj_ost.flight()

# This code demonstrates the concept of inheritance and method overriding in Python classes. 
# It shows how subclasses can override methods defined in their parent class to provide specific behavior 
# while still inheriting other methods from the parent class.


# Python Encapsulation
# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
# It describes the idea of wrapping data and the methods that work on data within one unit. 
# This puts restrictions on accessing variables and methods directly 
# and can prevent the accidental modification of data. 
# To prevent accidental change, an object’s variable can only be changed by an object’s method. 
# Those types of variables are known as private variables.

# A class is an example of encapsulation as it encapsulates all the data that is member functions, 
# variables, etc.

# Encapsulation in Python
print("__________________________________________________________")
print("Encapsulation in Python")
print("__________________________________________________________")

# Python program to
# demonstrate private members

# Creating a Base class
class Base:
	def __init__(self):
		self.a = "Coding Warriors"
		self.__c = "Warriors"

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a) # Coding Warriors

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class

# In the above example, we have created the c variable as the private attribute. 
# We cannot even access this attribute directly and can’t even change its value.


# Python in Data Abstraction 
# It hides unnecessary code details from the user. 
# Also, when we do not want to give out sensitive parts of our code implementation 
# and this is where data abstraction came.

# Data Abstraction in Python can be achieved by creating abstract classes.

print("__________________________________________________________")
print("Data Abstraction in Python")
print("__________________________________________________________")
# Import required modules
from abc import ABC, abstractmethod
 
# Create Abstract base class
class Car(ABC):
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
     
  # Create abstract method      
  @abstractmethod
  def printDetails(self):
    pass

  # Create concrete method
  def accelerate(self):
    print("speed up ...")
   
  def break_applied(self):
    print("Car stop")
     
# Create a child class
class Hatchback(Car):
   
  def printDetails(self):
    print("Brand:", self.brand)
    print("Model:", self.model)
    print("Year:", self.year)
   
  def Sunroof(self):
    print("Not having this feature")
     
# Create a child class
class Suv(Car):
   
  def printDetails(self):
    print("Brand:", self.brand)
    print("Model:", self.model)
    print("Year:", self.year)
   
  def Sunroof(self):
    print("Available")
 
     
car1 = Hatchback("Maruti", "Alto", "2022")
 
car1.printDetails()
car1.accelerate()
	

# Data hiding 
# In Python, we use double underscore (Or __) 
# before the attributes name and those attributes will not be directly visible outside. 

# A Python program to demonstrate that hidden 
# members can be accessed outside a class 
print("__________________________________________________________")
print("Data Hiding in Python")
print("__________________________________________________________")

class MyClass: 

	# Hidden member of MyClass 
	__hiddenVariable = 10

# Driver code 
myObject = MyClass()	 
print(myObject._MyClass__hiddenVariable) 


# Private methods are accessible outside their class, just not easily accessible.
# Nothing in Python is truly private; internally, the names of private methods and attributes 
# are mangled and unmangled on the fly to make them seem inaccessible by their given names



# Printing Objects 
# Printing objects give us information about objects we are working with.
# In C++, we can do this by adding a friend ostream& operator << (ostream&, const Foobar&) method for the class.
# In Java, we use toString() method.
# In python, this can be achieved by using __repr__ or __str__ methods.

print("__________________________________________________________")
print("Printing Objects in Python")
print("__________________________________________________________")

class Test: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

	def __repr__(self): 
		return "Test a:%s b:%s" % (self.a, self.b) 

	def __str__(self): 
		return "From str method of Test: a is %s," "b is %s" % (self.a, self.b) 

# Driver Code		 
t = Test(1234, 5678) 
print(t) # This calls __str__() 
print([t]) # This calls __repr__() 


# Important Points about Printing: 
# If no __str__ method is defined, print t (or print str(t)) uses __repr__. 

print("__________________________________________________________")

class Test: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

	def __repr__(self): 
		return "Test a:%s b:%s" % (self.a, self.b) 

# Driver Code		 
t = Test(1234, 5678) 
print(t) # Test a:1234 b:5678
print("__________________________________________________________")

# If no __repr__ method is defined then the default is used. 

class Test: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

# Driver Code		 
t = Test(1234, 5678) 
print(t) #<__main__.Test instance at 0x7fa079da6710>

print("__________________________________________________________")