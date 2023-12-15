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
# The student class has two member variables, name and age and a method display which prints the member 
# variable values.
# Both these variables and the methods are public as no specific keyword is assigned to them.
print('--------------Public Access Modifier------------------------')

class student:

    schoolName = 'XYZ School' # class attribute

    def __init__(self,name,age):
        self.name=name  # public data members or instance attribute 
        self.age=age  # public data members or instance attriribute
    
    def display(self): # public member function
        print('This is Public Method')
        print('Name :',self.name) 
        print('Age :',self.age)


stu=student('Harrish',22)
stu.display() # calling public member function of the class
print(stu.name) # accessing public data member
print(stu.schoolName) # class attribute or global varible
stu.age=21 # modify the public varible 
print(stu.age) 
print('------------------------------------------------------------')

# Private Access Modifier
# Python doesn't have any mechanism that effectively restricts access to any instance variable or method. 
# Python prescribes a convention of prefixing the name of the variable/method with a single or double underscore 
# to emulate the behavior of protected and private access specifiers.
# Class properties and methods with private access modifier can only be accessed within the class 
# where they are defined and cannot be accessed outside the class. 
# In Python private properties and methods are declared by adding a prefix with two underscores(‘__’) 
# before their declaration.
# private access modifier is the most secure access modifier.
# It gives a strong suggestion not to touch it from outside the class. 
# Any attempt to do so will result in an AttributeError:

print('-------------Private Access Modifier------------------------')
# Example for Private Modifier:
# The Class BankAccount is being declared with two private variables 
# i.e account_number and balance and a private property display_balance which prints the balance of the bank account. 
# As both the properties and method are private so while accessing them from outside the class it raises Attribute error.

class Bank:
    __HolderName = 'XYZ' # private class attribute

    def __init__(self,acc_no,balance):
        self.__account_no=acc_no  # private instance attribute
        self.__balance=balance # private instance attribute

    # private member function    
    def __display(self):  
	    print('This is private method.')
    
    # private member function  
    def __display_balance(self):
        # accessing private data members
        print("Bank Account_number: ", self.__account_no)
        print("Bank Balance: ", self.__balance)

    # public member function
    def accessPrivateFunction(self):
        print("Private method in public member function and display a private details")        
        # accessing private member function
        self.__display()
        self.__display_balance()  
        print('Private in public method : ',self.__HolderName) # print private varible 
 

bnk = Bank("0987654321", 25000)
# print(bnk.__HolderName) #AttributeError
# print(bnk.__account_no)   #AttributeError
# print(bnk.__display())  #AttributeError
# print(bnk.__display_balance())#AttributeError
bnk.accessPrivateFunction()

# In the above program, __account_no and __balance are private members, __display_balance(), __display method is a private
# member function (these can only be accessed within the class) and accessPrivateFunction() 
# method is a public member function of the class Bank which can be accessed from anywhere within the program. 
# The accessPrivateFunction() method accesses the private members of the class Bank.
print('------------------------------------------------------------')
print('name mangling of Private variables and method: ')
print(bnk._Bank__account_no)  #'0987654321'
bnk._Bank__account_no = 1234567890 # change the private variable
print(bnk._Bank__HolderName) #'Harrish'
bnk._Bank__display_balance() # display private method

# Name Mangling:
# Python performs name mangling of private variables. 
# Every member with a double underscore will be changed to _object._class__variable. 
# So, it can still be accessed from outside the class, but the practice should be refrained.
print('------------------------------------------------------------')



# Protected Members
# Protected members of a class are accessible from within the class and are also available to its sub-classes. 
# No other environment is permitted access to it. 
# This enables specific resources of the parent class to be inherited by the child class.
# Python's convention to make an instance variable protected is to add a prefix _ (single underscore) to it. 
# This effectively prevents it from being accessed unless it is from within a sub-class.

print('---------------Protected Access Modifier--------------------')

