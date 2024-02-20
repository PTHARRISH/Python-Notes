# Python self  
# Class methods must have an extra first parameter in the method definition. 
# We do not give a value for this parameter when we call the method, Python provides it
# If we have a method that takes no arguments, then we still have to have one argument.
# This is similar to this pointer in C++ and this reference in Java.
# When we call a method of this object as myobject.method(arg1, arg2), 
# this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – 
# this is all the special self is about.


# What is self in Python?
# Self represents the instance of the class. 
# By using the “self”  we can access the attributes and methods of the class in Python. 
# It binds the attributes with the given arguments. 
# The reason you need to use self. 
# because Python does not use the @ syntax to refer to instance attributes. 
# Python decided to do methods in a way that makes the instance to which the method belongs be passed automatically, 
# but not received automatically: the first parameter of methods is the instance the method is called on.


# Python Class self Constructor
# When working with classes, it’s important to understand that in Python, 
# a class constructor is a special method named __init__ that gets called 
# when you create an instance (object) of a class. 
# This method is used to initialize the attributes of the object. 
# Keep in mind that the self parameter in the constructor refers to the instance being created 
# and allows you to access and set its attributes. 
# By following these guidelines, you can create powerful and efficient classes in Python.


# Is self in Python a Keyword?
# No, ‘ self ‘ is not a keyword in Python. 
# Self is just a parameter name used in instance methods to refer to the instance itself.

# In a more clear way you can say that SELF has the following Characteristic-

# Self: Pointer to Current Object
# The self is always pointing to the Current Object. 
# When you create an instance of a class, 
# you’re essentially creating an object with its own set of attributes and methods.


print("To check the object address and self address")
# To check the object address and self address
class check:
	def __init__(self):
		print("Address of self = ",id(self)) # Address of self =  140273244381008

obj = check()
print("Address of class object = ",id(obj)) # Address of class object =  140273244381008


# Example: Creating Class with Attributes and Methods

# This code defines a Python class car representing cars with attributes ‘model’ and ‘color’. 
# The __init__ constructor initializes these attributes for each instance. 
# The show method displays model and color, while direct attribute access and method calls demonstrate 
# instance-specific data retrieval.

print("__________________________________________________________")

print("both objects have different self which contain their attributes")
class car():
	
	# init method or constructor
	def __init__(self, model, color):
		self.model = model
		self.color = color
		
	def show(self):
		print("Model is", self.model )
		print("color is", self.color )
		
# both objects have different self which contain their attributes
audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")

audi.show()	 # same output as car.show(audi)
ferrari.show() # same output as car.show(ferrari)

print("Model for audi is ",audi.model)
print("Colour for ferrari is ",ferrari.color)

# Output:
# Model is audi a4
# color is blue
# Model is ferrari 488
# color is green
# Model for audi is  audi a4
# Colour for ferrari is  green


# Self in Constructors and Methods
# Self is the first argument to be passed in Constructor and Instance Method.
# Self must be provided as a First parameter to the Instance method and constructor. 
# If you don’t provide it, it will cause an error.

# Self is always required as the first argument

print("__________________________________________________________")
# class check:
# 	def __init__():
# 		print("This is Constructor")

# object = check()
# print("Worked fine")

# Following Error is produced if Self is not passed as an argument
# Traceback (most recent call last):
# File "/home/c736b5fad311dd1eb3cd2e280260e7dd.py", line 6, in <module>
# 	object = check()
# TypeError: __init__() takes 0 positional arguments but 1 was given

# Self: Convention, Not Keyword
# Self is a convention and not a Python keyword. 
# Self is a parameter in Instance Method and the user can use another parameter name in place of it. 
# But it is advisable to use self because it increases the readability of code, 
# and it is also a good programming practice.

print("Self: Convention, Not Keyword")

class this_is_class: 
	def __init__(in_place_of_self): 
		print("we have used another "
		"parameter name in place of self") 
		
object = this_is_class() # we have used another parameter name in place of self

print("__________________________________________________________")
