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

# The definition of class is given below.

# class class_name:
#     Statement1_class
#     Statement2_class
#     Statement3_class
#     ………………………….
#     Statementn_class

# The statement in the class consists of either data or function.

# Class class_name:
#     Statements_classbody
#     def function_name(argument_list):
#         Statement_1
#         Statement_2
#         …………………..
#         Statement_n
# statements_classbody


# Creating an Empty Class in Python
# In the below example, we have created a class named employee using the class keyword.

class employee: 
    # class is a keyword to create a class. class name is employee
    #if you create a empty class it shows an error so you need to put pass statement on it(IndentationError: expected an indented block after class definition)
    pass



print("----------------------------Objects------------------------------")
# Python Objects:
# An object is called an instance of a class.
# The object is an entity that has a state and behavior associated with it.


# Creating an Object
# This will create an object named obj of the class employee defined above. 
# Before diving deep into objects and classes 
# let us understand some basic keywords that will we used while working with objects and classes.


emp1=employee()# each unique employee that we create using our employee class will be an instance of the class
emp2=employee()
print("Class employee Output printing Instance memory address : ")
print(emp1)# <__main__.employee object at 0x7fc5ca05bfd0> emp1 object memory address
print(emp2)# <__main__.employee object at 0x7fc5ca05beb0> emp2 object memory address
# Here emp1 and emp2 have unique employee classes


# In python, objects for classes can be created in two different ways. They are
#   ● Attribute referencing
#   ● instantiation.


print("-------------------Attribute Referencing----------------------")
# Attribute Referencing
# In attribute referencing, Python class properties can be accessed by using the class name itself. 
# The syntax of the attribute referencing is
# class_name.propertyname

# Example
class ex:
    x=[]
ex.x=input("Enter the value of member x: ") # Attribute Referencing
print("The value of ex.x is = ", ex.x)


print("-----------------------Instantiation---------------------------")
# Instantiation
# During the instantiation process, an empty object is created and this object is assigned with the given object name. 
# The syntax for the class instantiation is:  object_name = classs_name()

# After creating the class instantiation, the properties of the class are accessed with the following syntax
# object_name.propertyname
# Example

class ex:
    x=[]
a=ex()
a.x=input("Enter the value of member x: ") # Instantiation
print("The value of a.x is = ", a.x)
print("----------------------------------------------------------------")

# Example
# An example code for a class with members is given below.
class ex:
    x=100
    y="abcdefgh"
print("Member value of x=", ex.x)
print("Member value of y=", ex.y)

print("----------------------------------------------------------------")


# Example for car class:
print("Class Car Output : ")
class vehicle:

    no_of_wheels=0 # Global variable

    def __init__(self,type_of_vehicle,name,year_of_manufacture,model,top_speed,color):
        self.name=name # instance variable
        self.type= type_of_vehicle
        self.year_of_manufacture=year_of_manufacture
        self.model=model
        self.top_speed=top_speed
        self.color=color
        self.initial=0
        print(self.type)


    # def vehicle_details(self): # You can pass and change global variable
    #     global no_of_wheels # To modify global varible inside a function you need to declare (global keyword)
    #     no_of_wheels= wheels # or no_of_wheels=4  
    #     print("Local variable of no_of_wheels ",no_of_wheels) # print Local varible no_of_wheels
    #     print("vehicle brand name is {1} the model of the vehicle is {0} and top speed of vehicle is {2} ".format(self.model,self.name,self.top_speed) )
    #     print("Global variable no_of_wheels",self.no_of_wheels) # Print Global Variable inside a function you need to use self tag

    def start(self):
        print('vehicle started',self.initial) # here you no need to mention self in started_speed
    
    def speed_up(self,speed_up):
        self.initial+=speed_up
        print('vehicle speed is increased now vehicle speed is ',self.initial)

    def speed_down(self,speed_down):
        self.initial-=speed_down
        print('vehicle speed is reduced now vehicle speed is ',self.initial)
    
    def stop(self):
        self.initial=0
        print('vehicle stopped')

    
mercedes=vehicle('Car','mercedes','2018','ATVR','120mph','black')
# mercedes.vehicle_details()
print("vehicle Brand name is ",mercedes.name) # print Object variable (mercedes)
# print("No of wheels in car is ",mercedes.__class__.no_of_wheels) # print Global variable outside the class (4)
mercedes.start() # you can start speed and passed as an argument 
mercedes.speed_up(10)
mercedes.speed_up(10)
mercedes.speed_down(10)
mercedes.stop()
print("----------------------------------------------------------------")






