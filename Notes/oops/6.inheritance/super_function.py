# Python Super Function
# super() function is used to refer to the parent class or superclass. 
# It allows you to call methods defined in the superclass from the subclass, 
# enabling you to extend and customize the functionality inherited from the parent class.

# Syntax:
super(type, object)

# Parameters:
# type: (Optional) The class name whose base class methods needs to be accessed
# object: (Optional) An object of the class or self.

# Return type:
# No return value.
# Return a proxy object which represents the parent’s class.


# super() function in Python Example
# In the given example, 
# The Emp class has an __init__ method that initializes the id, and name and Adds attributes. 
# The Freelance class inherits from the Emp class and adds an additional attribute called Emails. 
# It calls the parent class’s __init__ method super() to initialize the inherited attribute.
print('--------- Super function to access variable from base class -----------------')

class Emp():
	def __init__(self, id, name, Add):
		self.id = id
		self.name = name
		self.Add = Add

# Class freelancer inherits EMP
class Freelance(Emp):
	def __init__(self, id, name, Address, Emails):
		super().__init__(id, name, Address) # calling base constructor.
		self.Emails = Emails

Emp_1 = Freelance(16, "Harrish", "SVKS" , "pt@gmail.com") # Passing the values to child constructor.
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)

# output:
# The ID is: 16
# The Name is: Harrish
# The Address is: SVKS
# The Emails is: pt@gmail.com


# What is the super () method used for?
# A method from a parent class can be called in Python using the super() function.
# It’s typical practice in object-oriented programming to call the methods of the superclass,
# and enable method overriding and inheritance. 
# Even if the current class has replaced those methods with its own implementation, 
# calling super() allows you to access and use the parent class’s methods. 
# By doing this, you may enhance and modify the parent class’s behavior while still gaining from it.


# Benefits of Super Function:
# Need not remember or specify the parent class name to access its methods. 
# This function can be used both in single and multiple inheritances.
# This implements modularity (isolating changes) and code reusability as there is no need to rewrite the entire function.
# The super function in Python is called dynamically because Python is a dynamic language, unlike other languages.


# The following example demonstrates how the derived class can call base class using the super() method.

print('--------- Super function to access variable and method from base class -----------------')

class person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def fullname(self):
        print(self.firstname,' ',self.lastname)
    
class student(person):
    def __init__(self, firstname, lastname, grade):
        self.grade = grade
        super().__init__(firstname, lastname) # calling base constructor
    def display_details(self):
        super().fullname() # calling base class method. so there is no need to rewrite the entire function 
        print('Grade',self.grade)
        
std = student('Harrish','PT', '16')
std.display_details()

print("----------------------------------------------------------------------------------------")
# In the above example, 
# super().__init__(firstname, lastname) in the init method of the student class call's the base class person's init method and pass parameters. 
# In the same way, super().fullname() calls person.fullname() method. 
# The super().fullname() can be called as super(student, self).fullname().

