# Python - Public, Protected, Private Members
# Access modifiers are used by object oriented programming languages like C++,java,python etc. 
# to restrict the access of the class member variable and methods from outside the class. 
# Encapsulation is an OOPs principle which protects the internal data of the class using Access modifiers 
# like Public,Private and Protected.
# Python supports three types of access modifiers which are public,private and protected. 
# These access modifiers provide restrictions on the access of member variables and methods of the class 
# from any object outside the class.

# Python uses ‘_’ symbol to determine the access control for a specific data member or a member function of a class. 
# Access specifiers in Python have an important role to play in securing data from unauthorized access 
# and in preventing it from being exploited.

# Public Access Modifier:
# By default the member variables and methods are public which means they can be accessed from anywhere outside 
# or inside the class.
# No public keyword is required to make the class or methods and properties public.
# Here is an example of Public access modifier −


class student:

    schoolName = 'XYZ School' # class attribute

    def __init__(self,name,age):
        self.name=name  # public data members or instance attribute 
        self.age=age  # public data members or instance attriribute
    
    def display(self): # public member function
        print('Name :',self.name)
        print('Age :',self.age)


stu=student('Harrish',22)
stu.display() # calling public member function of the class
print(stu.name) # accessing public data member
print(stu.schoolName) # class attribute or global varible
stu.age=21 # modify the public varible 
print(stu.age) 



