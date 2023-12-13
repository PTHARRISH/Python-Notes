# Python Private Method.
# In Python, we can define the private method by prefixing the single underscore to the method name,
# and like the other programming languages.
# we cannot prevent accessing the private method outside the class in python. 
# Simply we can say the private method is used only internally for the defined class.

# What is private method and public method?
# A private method is the method that should be called only inside the defined class,
# whereas the Public method is defined within the class, can be called on an instance of the defined class.

# Now let’s define the private method and see how the private method is differed from the public method.

# Example
# In this example we are going to create a base class by defining the public method and private methods 
# inside the class and after that we will check whether the private method can be accessible by the other class 
# or outside the class.

# Base class
class Base:
   # Defining the public method
   def pub(self):
      print("This is Public method")
   # Defining the private method
   def __priv(self):
      print("This is Private method")
# Now we are creating the derived class for calling the priivate and public methods created in the base class.
class Derived(Base):
   def __init__(self):
      Base.__init__(self)
   def call_pub(self):
   # Calling public method from base class
      print("\nInside derived class")
      self.pub()
   def call_priv(self):
   # Calling private method of base class
      self.__priv()
        
out = Base()
# Calling public method
out.pub()
out2 = Derived()
out2.call_pub()

