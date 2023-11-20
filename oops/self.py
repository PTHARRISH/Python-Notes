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
