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

