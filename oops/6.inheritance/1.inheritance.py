# Inheritance in Python
# One of the core concepts in object-oriented programming (OOP) languages is inheritance. 
# It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods 
# by deriving a class from another class. 
# Inheritance is the capability of one class to derive or inherit the properties from another class. 

# What is inheritance ?
# Inheritance allows us to create a new class from an existing class.
# The new class that is created is known as subclass (child or derived class) and 
# the existing class from which the child class is derived is known as superclass (parent or base class).

# Benefits of Inheritance in Python:
# It represents real-world relationships well.
# It provides the reusability of a code. 
# We don’t have to write the same code again and again. 
# Also, it allows us to add more features to a class without modifying it.
# It is transitive in nature, which means that if class B inherits from another class A, 
# then all the subclasses of B would automatically inherit from class A.
# Inheritance offers a simple, understandable model structure. 
# Less development and maintenance expenses result from an inheritance. 

# syntax for inheritance:
# define a superclass
# class super_class:
#     # attributes and method definition

# # inheritance
# class sub_class(super_class):
#     # attributes and method of super_class
#     # attributes and method of sub_class


print("__________________________________________________________")
print(" Example for Inheritance and Print Class ")
print("__________________________________________________________")
class ParentClass:
    pass

print(ParentClass) # <class '__main__.ParentClass'>

class ChildClass(ParentClass):
    pass

print(ChildClass) # <class '__main__.ChildClass'>

print("__________________________________________________________")

# In the above example, we created two classes, ChildClass and ParentClass. 
# Since ParentClass is passed as an argument to the ChildClass, ChildClass inherits the ParentClass.
# A child class in Python inherits all attributes, methods, and properties from its parent class.
print("Creating Parent and Child Class")
print("__________________________________________________________")

# Creating a Parent Class
# A parent class is a class whose properties are inherited by the child class. 
# Let’s create a parent class called Person which has a Display method to display the person’s information.

# A Python program to demonstrate inheritance
# Creating Parent and Child Class
class Person(object):

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.roll_no = id

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.roll_no)


# Driver code
emp = Person("Harrish", 16) # An Object of Person
emp.Display() # Harrish 16


# Creating a Child Class
# A child class is a class that drives the properties from its parent class. 
# Here Emp is another class that is going to inherit the properties of the Person class(base class).
class Emp(Person):

    def Print(self):
        print("Emp class called")
	
Emp_details = Emp("Kishore", 19)

# calling parent class function
Emp_details.Display() # Kishore 19

# Calling child class function
Emp_details.Print() # Emp class called

# In this example, ‘Person’ is the parent class, and ‘Emp’ is its child class.


# Subclassing (Calling constructor of parent class) :
# A child class needs to identify which class is its parent class. 
# This can be done by mentioning the parent class name in the definition of the child class. 

# Example: class subclass_name (superclass_name)


print("__________________________________________________________")
# Python code to demonstrate how parent constructors
# are called.
print("Subclassing (Calling constructor of parent class) : ")

print("__________________________________________________________")
# parent class
class Person(object):

	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)

# child class
class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		Person.__init__(self, name, idnumber)

# creation of an object variable or an instance
a = Employee('Harrish', 886012, 200000, "Backend-Intern")

# calling a function of the class Person using its instance
a.display()


# In this example, ‘a’ is the instance created for the class Person. 
# It invokes the __init__() of the referred class. 
# You can see ‘object’ written in the declaration of the class Person. 
# In Python, every class inherits from a built-in basic class called ‘object’. 
# The constructor i.e. the ‘__init__’ function of a class is invoked 
# when we create an object variable or an instance of the class.

