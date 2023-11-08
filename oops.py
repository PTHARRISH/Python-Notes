# Variables
a=10 # assign 10 to variable a
b=10 # assign 10 to variable b

# id():
# id() function is a built-in function that returns the unique identifier of an object.
# The identifier is an integer, which represents the memory address of the object.
# The id() function is commonly used to check if two variables or objects refer to the same memory location.
print(id(a))#a and b have same value the memory location will be same displayed.
print(id(b))

# class:
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.
# A class is a user-defined blueprint or prototype from which objects are created.
# Classes provide a means of bundling data and functionality together. 
# Creating a new class creates a new type of object, allowing new instances of that type to be made.

class employee: 
    # class is a keyword to create a class. class name is employee
    #if you create a empty class it shows an error so ypu need to put pass statement on it
    pass

emp1=employee()# each unique employee that we create using our employee class will be an instance of the class
emp2=employee()
print(emp1)# <__main__.employee object at 0x7fc5ca05bfd0> emp1 object memory address
print(emp2)# <__main__.employee object at 0x7fc5ca05beb0> emp2 object memory address


# object:
# An object is called an instance of a class.here emp1 and emp2 have unique employee classes


# pass: 
# The pass statement is used as a placeholder for future code. 
# When the pass statement is executed, nothing happens, but you avoid getting an error 
# when empty code is not allowed.
# Empty code is not allowed in loops, function definitions, class definitions, or in if statements



class my_class:
    # global variable
    strength='empty'
    classroom='None'
    a=20

    def __init__(self,class_name="None",staff="Unallotted",fullname="None"):
    # self : Pointer to Current Object. staff=None is default arguments
        self.staff_name=staff # Instance variable creating automatically
        self.fullname=fullname
        self.classroom=class_name
        print(a)
        print(self.staff_name,self.fullname,self.classroom)


    def myclass(self,student): # without self keyword positional argument error occurs
        global strength # access the global variable change inside a function
        strength=student# it will work inside the 
        return  "Total strength of the class is " +strength # return statement store the value in the the function on it 
        
    def myfunct(self,repname):
        #local variable
        rep=repname
        print(self.classroom," incharge staff ",self.staff_name," full name ",self.fullname)
        print(rep+" is representative for " +self.classroom)
        print(self.strength+" students inside the class room ")
        #self.strength show class variable strength if current obj not available it will take global variable




obj=my_class("I MCA","HPT","Harrish PT") 
# object creation for class (my_class is Class name).obj is instance of the class or object
# you can't pass global variable inside class  

# print(obj) 
# print memory address of the object (obj)

print(obj.strength) 
# Print obj.name is Global Variable (my_class.name)

obj.staff_name="KK"
obj.fullname="Kishore" 
# Manually created instance variable 

print("Manually created staff name : "+obj.staff_name) 
print("Manually created staff fullname : "+obj.fullname) 
# printing Manually created instance variable 

print(obj.myclass('16')) 
# It will print inside the myfunc stored value //Roll16

obj.myclass('15') 
# It will not print anything if you call the function without print statement it will print Nothing

obj.myfunct('Harrish')
# Here It will print the value because in myfunct contain print statement inside on it so no need to again use print function

obj2=my_class("I MCA",'Dk','Dineshkumar') # create a object and pass a value to the constructor or __init__ method
obj2.myfunct('Santhosh')

# Instance variable:
# Instance variable contains data that is unique to each instance.
# Instance variable can created manually and automatically. 
# Manually set the variables every time its a lots of code and it also prone to mistake.


# self
# the term “self” refers to the instance of the class that is currently being used. 
# It is customary to use “self” as the first parameter in instance methods of a class.
# Whenever you call a method of an object created from a class, 
# the object is automatically passed as the first argument using the “self” parameter. 
# The self is always pointing to the Current Object. 
# When you create an instance of a class, 
# you’re essentially creating an object with its own set of attributes and methods.


# constructor
# a class constructor is a special method named __init__ that gets called when you create an instance (object) of a class. 
# This method is used to initialize the attributes of the object. 
# Keep in mind that the self parameter in the constructor refers to the instance being created and allows 
# you to access and set its attributes. 

class my_class1:
    # global variable

    def __init__(self):
        a=10
        b=20
    # self : Pointer to Current Object. staff=None is default argument
        print(a+b)
s1=my_class1()
    
