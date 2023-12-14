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



# Creating Lists
# You can create a list by enclosing its elements in square brackets [], separated by commas:

my_list = [1, 2, 3, 4, 5]

# Or you can create an empty list and then add elements to it later:

my_list = []
my_list.append(1)
my_list.append(2)


# Accessing Elements
# You can access elements in a list by their index, starting from 0 for the first element:

first_element = my_list[0]  # Gets the first element (1 in this case)


# Modifying Elements
# As lists are mutable, you can change their elements:

my_list[0] = 10  # Changes the first element to 10


# Slicing Lists
# You can also take slices of lists to get new lists containing subsets of elements:

sub_list = my_list[1:4]  # Gets elements from index 1 to 3


# Useful Methods

# append(): Adds an element to the end of the list.

# clear(): Remove all items from the list.

# copy(): Return a copy of the list. 

# count(): Return the count of the number of items passed as an argument.

# extend(): Add all element of a list to another list.

# index(): Return the index of the first matched item.

# insert(): Adds an element at a specific index.

# pop(): Removes the element at a specific index.

# remove(): Removes the first occurrence of a value.

# reverse(): Reverses the list.

# sort(): Sorts the list.



# Example:
# Here's a small example that demonstrates some of these features:

# Creating a list
my_list = [1, 2, 3, 4, 5]
 
# Accessing elements
print(my_list[0])  # Output: 1
 
# Modifying elements
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]
 
# Slicing list
print(my_list[1:4])  # Output: [2, 3, 4]
 
# Using methods
my_list.append(6)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]


# Lists are an essential part of Python, and knowing how to use them effectively is crucial 
# for many programming tasks.

