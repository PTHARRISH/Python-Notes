# Introduction to OOPS concept:
# Python supports both procedure-oriented and object-oriented features.
# Object-Oriented Programming is a programming paradigm that uses classes and objects to look similar to real life. 

# OOPs has four central concepts: 
#   Encapsulation.
#   Abstraction.
#   Inheritance. 
#   Polymorphism.
# OOPs mainly works upon two keys is Attributes and Functionality.

# Python Class  :
# A class is a collection of objects.
# A class contains the blueprints or the prototype from which the objects are being created. 
# It is a logical entity that contains some attributes and methods. 

# To understand the need for creating a class 
# let’s consider an example,
# let’s say you wanted to track the number of dogs that may have different attributes like breed, and age. 
# If a list is used, the first element could be the dog’s breed while the second element could represent its age. 
# Let’s suppose there are 100 different dogs, 
# then how would you know which element is supposed to be which? 
# What if you wanted to add other properties to these dogs? 
# This lacks organization and it’s the exact need for classes.
 

# Some points on Python class:  
# Classes are created by keyword class.
# Attributes are the variables that belong to a class.
# Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute


# Creating an Empty Class in Python
# Python3 program to demonstrate defining a class

class Dog:
	pass

# In the above example, we have created a class named Dog using the class keyword.


# Python Objects
# The object is an entity that has a state and behavior associated with it. 
# It may be any real-world object like a mouse, keyboard, chair, table, pen, etc. 
# Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects. 
# More specifically, any single integer or any single string is an object. 
# The number 12 is an object, the string “Hello, world” is an object, 
# a list is an object that can hold other objects, and so on. 
# You’ve been using objects all along and may not even realize it.

# An object consists of:
# State: It is represented by the attributes of an object. It also reflects the properties of an object.
# Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
# Identity: It gives a unique name to an object and enables one object to interact with other objects.

# To understand the state, behavior, and identity let us take the example of the class dog (explained above). 
# The identity can be considered as the name of the dog.
# State or Attributes can be considered as the breed, age, or color of the dog.
# The behavior can be considered as to whether the dog is eating or sleeping.


# Creating an Object
# This will create an object named obj of the class Dog defined above. 
# Before diving deep into objects and classes 
# let us understand some basic keywords that will we used while working with objects and classes.

# Example for creating object for class
obj = Dog()


# Python self  
# Class methods must have an extra first parameter in the method definition. 
# We do not give a value for this parameter when we call the method, Python provides it
# If we have a method that takes no arguments, then we still have to have one argument.
# This is similar to this pointer in C++ and this reference in Java.
# When we call a method of this object as myobject.method(arg1, arg2), 
# this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – 
# this is all the special self is about.


# The Python __init__ Method 
# The __init__ method is similar to constructors in C++ and Java. 
# It is run as soon as an object of a class is instantiated. 
# The method is useful to do any initialization you want to do with your object. 
# Now let us define a class and create some objects using the self and __init__ method.


# Creating a class and object with class and instance attributes
class Dog:

	# class attribute
	attr1 = "mammal"

	# Instance attribute
	def __init__(self, name):
		self.name = name


# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1)) # mammal
print("Tommy is also a {}".format(Tommy.__class__.attr1)) # mammal

# Accessing instance attributes
print("My name is {}".format(Rodger.name)) # Rodger
print("My name is {}".format(Tommy.name)) # Tommy

# Creating Classes and objects with methods
# Here, The Dog class is defined with two attributes:

# attr1 is a class attribute set to the value “mammal”.
# Class attributes are shared by all instances of the class.
# __init__ is a special method (constructor) that initializes an instance of the Dog class. 

# It takes two parameters: 
# self (referring to the instance being created) and name (representing the name of the dog). 
# The name parameter is used to assign a name attribute to each instance of Dog.
# The speak method is defined within the Dog class. 
# This method prints a string that includes the name of the dog instance.


# The driver code starts by creating two instances of the Dog class: Rodger and Tommy. 
# The __init__ method is called for each instance to initialize their name attributes with the provided names. 
# The speak method is called in both instances (Rodger.speak() and Tommy.speak()), 
# causing each dog to print a statement with its name.