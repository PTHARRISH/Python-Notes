# Name mangling in Python
# Name mangling with double underscores
# If you prefix an attribute name with double underscores (__) like this:

# __attribute
# Python will automatically change the name of the __attribute to:

# _class__attribute
# This is called the name mangling in Python.

# By doing this, you cannot access the __attribute directly from the outside of a class like:

# instance.__attribute
# Code language: CSS (css)
# However, you still can access it using the _class__attribute name:

# instance._class__attribute

# The following example redefines the Counter class with the __current attribute:

class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0


# Now, if you attempt to access __current attribute, you’ll get an error:

counter = Counter()
print(counter.__current)

# Output:
# AttributeError: 'Counter' object has no attribute '__current'


# However, you can access the __current attribute as _Counter___current like this:

counter = Counter()
print(counter._Counter__current)
