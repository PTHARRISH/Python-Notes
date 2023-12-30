# list - Introduction :

# In Python, a list is a built-in data structure that can store multiple items in a single variable. 
# Lists are ordered, mutable, and allow duplicate items. 
# They are one of the most versatile and commonly used data structures in Python, 
# and they are useful for a variety of tasks, 
# such as grouping together related data or storing sequences of elements.

# Characteristics of List:

# Ordered: The elements in a list have a specific order that is maintained.

# Mutable: You can modify the contents of a list after it has been created.

# Allows Duplicate Members: A list can have two or more elements that are identical.

# Heterogeneous: Lists can contain elements of different types, although this is generally not recommended for most applications.
print("-----------------------------------------------------------")



# Creation of Lists object
# You can create a list by enclosing its elements in square brackets [], separated by commas:

my_list = [1, 2, 3, 4, 5]
print(my_list) # [1, 2, 3, 4, 5]
print("print the type of my_list",type(my_list)) # <class 'list'>

# Or you can create an empty list and then add elements to it later:

my_list = []
print("creating the empty list",my_list)
my_list.append(1)
print("Appending element in a list",my_list)


# Accessing Elements
# You can access elements in a list by their index, starting from 0 for the first element:

first_element = my_list[0]  # Gets the first element (1 in this case)
print("Accessing Elements",first_element)


# Modifying Elements
# As lists are mutable, you can change their elements:

my_list[0] = 10  # Changes the first element to 10
print("Modifying Elements", my_list)


# Checking the elements
# using in keyword the element are present or not in list will be checked and return True or False

print("10 in my_list", 10 in my_list) # True
print( "11 in my_list",11 in my_list) # False

print("-----------------------------------------------------------")
