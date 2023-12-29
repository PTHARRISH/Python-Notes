# Python __init__ Method 
# The __init__ method is similar to constructors in C++ and Java. 
# It is run as soon as an object of a class is instantiated. 
# The method is useful to do any initialization you want to do with your object. 
# Now let us define a class and create some objects using the self and __init__ method.

# What is __init__ in Python?
# The Default __init__ Constructor in C++ and Java. 
# Constructors are used to initializing the object’s state. 
# The task of constructors is to initialize(assign values) to the data members of the 
# class when an object of the class is created. 
# Like methods, a constructor also contains a collection of statements (i.e. instructions) that are executed 
# at the time of Object creation. 
# It is run as soon as an object of a class is instantiated. 
# The method is useful to do any initialization you want to do with your object.
# The constructor method should always take the self pointer as the first argument. 
# The remaining arguments will be passed during the object creation. 

# Constructors are generally used for instantiating an object. 
# The task of constructors is to initialize(assign values)
# to the data members of the class when an object of the class is created. 
# In Python the __init__() method is called the constructor and is always called when an object is created.

# Syntax of constructor declaration : 

def __init__(self):
    pass
    # body of the constructor


# Types of constructors : 
# default constructor: 
# The default constructor is a simple constructor which doesn’t accept any arguments. 
# Its definition has only one argument which is a reference to the instance being constructed.


# parameterized constructor: 
# constructor with parameters is known as parameterized constructor. 
# The parameterized constructor takes its first argument as a reference 
# to the instance being constructed known as self and the rest of the arguments are provided by the programmer.


# Example:
class ex:
	def __init__(self, arg):
		self.a=arg
obj=ex(300)
print("Value defined by the constructor=", obj.a)
# Output:
# Value defined by the constructor= 300


print("-----------------------------------------------------------------------------")
print(" Example for Types of Constructor ")
print("-----------------------------------------------------------------------------")
class MyClass:
	def __init__(self, name=None):
		if name is None:
			print("Default constructor called")
		else:
			self.name = name
			print("Parameterized constructor called with name", self.name)
	
	def method(self):
		if hasattr(self, 'name'):
			print("Method called with name", self.name)
		else:
			print("Method called without a name")

# Create an object of the class using the default constructor
obj1 = MyClass() # Default constructor called

# Call a method of the class
obj1.method() # Method called without a name

# Create an object of the class using the parameterized constructor
obj2 = MyClass("John") # Parameterized constructor called with name

# Call a method of the class
obj2.method()  # 'Method called with name', 'John'

print("-----------------------------------------------------------------------------")

# __init__ with inheritance
# Inheritance is the capability of one class to derive or inherit the properties from some other class. 
# Let’s consider the below example to see how __init__ works in inheritance. 


print("Python program to demonstrate init with inheritance")
print("-----------------------------------------------------------------------------")
class A(object):
	def __init__(self, something):
		print("A init called")
		self.something = something


class B(A):
	def __init__(self, something):
		# Calling init of parent class
		A.__init__(self, something)
		print("B init called")
		self.something = something
		print(self.something)


obj = B("Something")



# Advantages of using constructors in Python:
# Initialization of objects: 
# Constructors are used to initialize the objects of a class. 
# They allow you to set default values for attributes or properties, 
# and also allow you to initialize the object with custom data.
# 
# Easy to implement: 
# Constructors are easy to implement in Python, and can be defined using the __init__() method.
# 
# Better readability: 
# Constructors improve the readability of the code by making it clear what values are being initialized 
# and how they are being initialized.
# 
# Encapsulation: 
# Constructors can be used to enforce encapsulation, by ensuring that the object’s attributes are initialized
# correctly and in a controlled manner.

# Disadvantages of using constructors in Python:
# Overloading not supported: 
# Unlike other object-oriented languages, Python does not support method overloading. 
# This means that you cannot have multiple constructors with different parameters in a single class.
# 
# Limited functionality: 
# Constructors in Python are limited in their functionality compared to constructors in other programming languages. 
# For example, Python does not have constructors with access modifiers like public, private or protected.
# 
# Constructors may be unnecessary: 
# In some cases, constructors may not be necessary, as the default values of attributes may be sufficient. 
# In these cases, using a constructor may add unnecessary complexity to the code.
# 
# Overall, constructors in Python can be useful for initializing objects and enforcing encapsulation. 
# However, they may not always be necessary and are limited in their functionality compared to constructors in other programming languages.


print("-------------------------------Destructor-------------------------------------")
# Destructor
# In python programming, the __del__() method will be executed during objects get destroyed. 
# When a program is finished execution, all the objects are managed by memory management automatically. 
# The __del__() method is called when all references to the object have been deleted.

# Example:
class ex:
	def __init__(self, arg):
		self.a=arg
	def __del__(self):
		print("Object is deleted.")

obj=ex(300)
print("Value defined by the constructor=", obj.a)
# del obj # If you not call __del__ it automatically call atlast of the program
print("-----------------------------------------------------------------------------")

class sample:
    def __init__(self, n):
        self.a=n
        print(self.a, "object created", end=" ")
    def __del__(self):
        print(self.a, "object deleted", end=" ")
obj1=sample(1)
obj2=sample(2)
print("-----------------------------------------------------------------------------")
