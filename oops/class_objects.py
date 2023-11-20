# Class:
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# A class is a user-defined blueprint or prototype from which objects are created. 
# Classes provide a means of bundling data and functionality together. 
# Creating a new class creates a new type of object, allowing new instances of that type to be made. 
# Each class instance can have attributes attached to it for maintaining its state. 
# Class instances can also have methods (defined by their class) for modifying their state.

# The class creates a user-defined data structure, which holds its own data members and member functions, 
# which can be accessed and used by creating an instance of that class. 

# Some points on Python class:
# Classes are created by keyword class.
# Attributes are the variables that belong to a class.
# Attributes are always public and can be accessed using the dot (.) operator.
# Classes consist of Data and Functions. 
# The Data in class is known as Members and functions of the class are known as methods.

# Objects are real-world entities while classes are not real.

# Creating an Empty Class in Python
# In the below example, we have created a class named employee using the class keyword.

class employee: 
    # class is a keyword to create a class. class name is employee
    #if you create a empty class it shows an error so you need to put pass statement on it(IndentationError: expected an indented block after class definition)
    pass


# Python Objects:
# An object is called an instance of a class.
# The object is an entity that has a state and behavior associated with it.
# It may be any real-world object like a mouse, keyboard, chair, table, pen, etc. Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects. 
# More specifically, any single integer or any single string is an object. 
# The number 12 is an object, the string “Hello, world” is an object, a list is an object that can hold other objects, and so on. 
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
# This will create an object named obj of the class employee defined above. 
# Before diving deep into objects and classes let us understand some basic keywords that will we used while working with objects and classes.


emp1=employee()# each unique employee that we create using our employee class will be an instance of the class
emp2=employee()
print(emp1)# <__main__.employee object at 0x7fc5ca05bfd0> emp1 object memory address
print(emp2)# <__main__.employee object at 0x7fc5ca05beb0> emp2 object memory address

# Here emp1 and emp2 have unique employee classes

# Example for car class:

class car:
    def __init__(self,year_of_manufacture,model,top_speed,color):
        self.year_of_manufacture=year_of_manufacture
        self.model=model
        self.top_speed=top_speed
        self.color=color
        self.initial=0
    
    def start(self):
        print('car started',self.initial) # here you no need to mention self in started_speed
    
    def speed_up(self,speed_up):
        self.initial+=speed_up
        print('car speed is increased now car speed is ',self.initial)

    def speed_down(self,speed_down):
        self.initial-=speed_down
        print('car speed is reduced now car speed is ',self.initial)
    
    def stop(self):
        self.initial=0
        print('car stopped')

    
mercedes=car('2018','ATVR','120mph','black')
mercedes.start() # you can start speed and passed as an argument 
mercedes.speed_up(10)
mercedes.speed_up(10)
mercedes.speed_down(10)
mercedes.stop()






