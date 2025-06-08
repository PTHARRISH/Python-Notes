# Operator Overloading 
# Operator overloading is a feature that allows us to define the behavior of operators 
# for user-defined classes.
# In Python, we can overload operators by defining special methods in our class.
# These special methods are also known as magic methods or dunder methods (double underscore methods).
# The special methods for operator overloading are defined with double underscores 
# before and after the method name.
# For example, to overload the addition operator (+), we define the __add__ method in our class.
# Other in arguments are passed to the method as parameters.
# The first argument is always self, which refers to the instance of the class.
# The second argument is the object that we are adding to the first object.
# We can also overload other operators like -, *, /, %, //, **, ==, !=, <, >, <=, >=, etc.

# Here is an example of operator overloading in Python:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Overloading the - operator
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # Overloading the * operator
    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    # Overloading the / operator
    def __truediv__(self, scalar):
        return Point(self.x / scalar, self.y / scalar)

    # Overloading the str() function
    def __str__(self):
        return f"({self.x}, {self.y})"
    
# Example usage
p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2  # Calls __add__
p4 = p1 - p2  # Calls __sub__
p5 = p1 * 2   # Calls __mul__
p6 = p1 / 2   # Calls __truediv__
print(p3)  # Output: (6, 8)
print(p4)  # Output: (-2, -2)
print(p5)  # Output: (4, 6)
print(p6)  # Output: (1.0, 1.5)
# In this example, we have defined a Point class that represents a point in 2D space.
# We have overloaded the +, -, *, and / operators to perform addition, subtraction, multiplication, and division on Point objects.
# The __str__ method is also overloaded to provide a string representation of the Point object.
# This allows us to use the operators with Point objects just like we would with built-in types.
# Operator overloading is a powerful feature that allows us to create more intuitive and readable code.
# It allows us to define the behavior of operators for our custom classes, making them behave like built-in types.
# This can make our code more readable and easier to understand.
# However, it is important to use operator overloading judiciously and not to overload operators in a way that is confusing or unexpected.
# In general, operator overloading should be used to make the code more intuitive and readable.
# It should not be used to create unexpected behavior or to make the code more complex.