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
print("---------------------outside the class---------------------")
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
print('-----------------------------------------------')
print('name mangling of Private variables and method: ')
print("---------------outside the class---------------")
print(bnk._Bank__account_no)  #'0987654321'
bnk._Bank__account_no = 1234567890 # change the private variable
print(bnk._Bank__HolderName) #'Harrish'
bnk._Bank__display_balance() # display private method

# Read a Name Mangling :
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


# Example
# The Person class has two protected properties i.e _name and _age and a protected method _display that 
# displays the values of the properties of the person class. 
# The student class is inherited from Person class with an additional property 
# i.e _roll_number which is also protected and a public method display that class the _display 
# method of the parent class 
# i.e Person class by creating an instance of the Student class we can call the display method from 
# outside the class as the display method is private which calls the protected _display method of Person class.

class Person: # parent class
   def __init__(self, name, age):
      self._name = name # Protected attribute
      self._age = age # Protected attribute
    
    # Protected method
   def _display(self): 
      print("Name:", self._name)
      print("Age:", self._age)

class Student(Person): # child class
   def __init__(self, name, age, roll_number):
      super().__init__(name, age) # or ypu can use Person.__init__(self,name,age) 
      self._roll_number = roll_number # Protected attribute
    
   def display(self):
      self._display() # accessing protected member function
      print("Roll Number:", self._roll_number)

s = Student("Harrish", 22, 16)
s.display() # Name: Harrish Age: 22 Roll Number: 16
print("--------------outside the class--------------")
print(s._roll_number) # display roll no :16
s._name="Harrish PT"
print(s._name) # display name : "Harrish PT"


# Read Property Decorator
# However, you can define a property using property decorator and make it protected, as shown below.

# Example: Protected Attributes
print('---------------Protected Using @property decorator--------------------')
class Student:
    _name=None
    _age=None
    def __init__(self,name,age):
        self._name=name
        self._age=age
    
    @property
    def names(self):
        return self._name
    
    @names.setter
    def names(self,new_name):
        self._name=new_name
        return self._name

std=Student("Harrish",22)
print("--------------outside the class--------------")
print(std._name) # Harrish
print("-------------@property decorator-------------")
std.names="Harrish PT" # obj.function name= value
print(std._name)
print("---------------------------------------------")
# Above, @property decorator is used to make the names() method as property and @names.
# setter decorator to another overloads of the names() method as property setter method. 
# Now, _name is protected.
# we used std.name property to modify _name attribute. 
# However, it is still accessible in Python. 
# Hence, the responsible programmer would refrain from accessing and modifying instance variables 
# prefixed with _ from outside its class.
 

#  Example program for three access modifiers (public, protected, and private) of a class in Python: 
print("--Example program for three access modifiers--")
class Bank:

    name=None # Public attribute
    _account_no=None # Protected attribute
    __balance=None # Private attribute

    def __init__(self,name,account_no,balance):
        self.name=name
        self._account_no=account_no
        self.__balance=balance
    
    # Display Public method and Public variable.
    def display(self):
        print("Name: ",self.name)
        
    # Display Protected method and Protected variable.
    def _display_protected(self):
        print("account no: ",self._account_no)
    
    # Display Private method and Private variable.
    def __display_private(self):
        print("Balance: ",self.__balance)
        
    # Display Private variable in Public method.   
    def accessprivatefunction(self):
        self.__display_private()

class Person(Bank):

    def __init__(self, name, account_no, balance,branch):
        super().__init__(name, account_no, balance)
        self.__branch=branch # Private variable
        
    def profile(self):
        self.display() # call base class function print public variable
        self.accessprivatefunction() # call base class public function print private variable
        self._display_protected() # call base class function print public variable

    def accessprivate(self):
        print("branch: ",self.__branch) # print private variable

obj=Person("Harrish PT",123334087,123,"SVKS")
print("--------Print all variable using functions--------")
obj.profile() # print all account details.
obj.accessprivate() # Access and print Private variable using function .
print("-------Modify all variable outside a class--------")
obj.name="Hash"  # Access Public variable.
obj._account_no=12344556  # Access Protected variable.
obj._Bank__balance=1233  # Access Private variable.
print("Name: ",obj.name) # Print Public variable.
print("Account_no: ",obj._account_no) # Print Protected variable.
print("Balance: ",obj._Bank__balance) # Print Private variable using name mangling.
print("Branch: ",obj._Person__branch) # Print Private variable using name mangling.
print("--------------------------------------------------")

        
