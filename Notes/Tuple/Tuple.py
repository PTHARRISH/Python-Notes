print("------------------------------------------------------------------------------------------")
print("-------------------------------------Tuple------------------------------------------------")
print("------------------------------------------------------------------------------------------")

# Tuple
# A tuple is a collection of ordered elements that can be of different data types.
# Tuples are immutable, meaning that once they are created, their elements cannot be changed.
# Tuples are defined using parentheses () and can contain any number of elements.
# Tuples can also be nested, meaning that a tuple can contain other tuples as elements.
# Tuples are similar to lists, but they are immutable, 
# meaning that their elements cannot be changed after they are created.
# Tuples are often used to group related data together,
# such as coordinates (x, y) or RGB color values (red, green, blue).
# Tuples can also be used as keys in dictionaries,
# while lists cannot be used as keys in dictionaries because they are mutable.
# Tuples are also more memory efficient than lists,
# making them a better choice for storing large amounts of data.
# time complexity of tuple is O(1) for accessing elements,
# O(n) for searching elements, and O(n) for iterating through the elements.
# Tuples are also faster than lists for certain operations,
# such as concatenation and repetition.
# Tuples are also hashable, meaning that they can be used as keys in dictionaries,
# while lists are not hashable and cannot be used as keys in dictionaries.
# Tuples are also more memory efficient than lists,
# making them a better choice for storing large amounts of data.

# Methods of Tuple
# 1. count() - Returns the number of occurrences of a specified value in a tuple.
# 2. index() - Returns the index of the first occurrence of a specified value in a tuple.
# 3. len() - Returns the number of elements in a tuple.
# 4. max() - Returns the largest element in a tuple.
# 5. min() - Returns the smallest element in a tuple.
# 6. sum() - Returns the sum of all elements in a tuple.
# 7. sorted() - Returns a sorted list of the elements in a tuple.
# 8. all() - Returns True if all elements in a tuple are true (or if the tuple is empty).
# 9. any() - Returns True if any element in a tuple is true. If the tuple is empty, returns False.
# 10. tuple() - Converts an iterable (like a list) into a tuple.
# 11. zip() - Combines two or more tuples into a single tuple of tuples.
# 12. enumerate() - Returns an enumerate object, which contains pairs of index and value from the tuple.
# 13. reversed() - Returns a reversed iterator of the tuple.
# 14. map() - Applies a function to all items in the tuple and returns a new tuple.
# 15. filter() - Filters elements from the tuple based on a function and returns a new tuple.
# 16. repeat() - Repeats the elements of a tuple a specified number of times.
# 17. unpacking - Unpacks the elements of a tuple into separate variables.
# 18. slicing - Returns a new tuple that contains a portion of the original tuple.
# 19. concatenation - Combines two or more tuples into a single tuple.
# 20. repetition - Repeats the elements of a tuple a specified number of times.
# 21. membership - Checks if an element is present in a tuple.
# 22. iteration - Iterates through the elements of a tuple.
# 23. copying - Creates a shallow copy of a tuple.
# 24. deep copying - Creates a deep copy of a tuple.
# 25. sorting - Sorts the elements of a tuple and returns a new tuple.
# 26. reversing - Reverses the elements of a tuple and returns a new tuple.
# 27. converting - Converts a tuple to a list and vice versa.
# 28. packing - Packs multiple values into a tuple.

# Example of Tuple
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Accessing elements in a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Slice of tuple:", my_tuple[1:4])
print("Tuple length:", len(my_tuple))

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print("Concatenated tuple:", tuple3)

# Repeating tuples
tuple4 = tuple1 * 3
print("Repeated tuple:", tuple4)

# Unpacking tuples
a, b, c = tuple1
print("Unpacked values:", a, b, c)

# Nested tuples
nested_tuple = (1, (2, 3), (4, 5))
print("Nested tuple:", nested_tuple)

# Accessing nested tuple elements
print("Nested tuple element:", nested_tuple[1][0])
print("Nested tuple length:", len(nested_tuple[1]))

# Tuple methods
# Count method
count_tuple = (1, 2, 3, 1, 4, 5)
print("Count of 1 in tuple:", count_tuple.count(1))

# Index method
print("Index of 3 in tuple:", count_tuple.index(3))

# Max method
print("Max element in tuple:", max(count_tuple))

# Min method
print("Min element in tuple:", min(count_tuple))

# Sum method
print("Sum of elements in tuple:", sum(count_tuple))

# Sorted method
print("Sorted tuple:", sorted(count_tuple))

# All method
print("All elements are true:", all(count_tuple))

# Any method
print("Any element is true:", any(count_tuple))

# Tuple conversion
list_to_tuple = [1, 2, 3, 4, 5]
tuple_from_list = tuple(list_to_tuple)
print("Tuple from list:", tuple_from_list)

# Zip method
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
zipped_tuple = zip(tuple1, tuple2)
print("Zipped tuple:", list(zipped_tuple))

# Enumerate method
tuple1 = (1, 2, 3)
enumerated_tuple = enumerate(tuple1)
print("Enumerated tuple:", list(enumerated_tuple))

# Reversed method
tuple1 = (1, 2, 3)
reversed_tuple = reversed(tuple1)
print("Reversed tuple:", list(reversed_tuple))

# Map method
def square(x):
    return x * x
tuple1 = (1, 2, 3)
mapped_tuple = map(square, tuple1)
print("Mapped tuple:", tuple(mapped_tuple))

# Filter method
def is_even(x):
    return x % 2 == 0
tuple1 = (1, 2, 3, 4, 5)
filtered_tuple = filter(is_even, tuple1)
print("Filtered tuple:", tuple(filtered_tuple))

# Repeat method
from itertools import repeat
tuple1 = (1, 2, 3)
repeated_tuple = repeat(tuple1, 3)
print("Repeated tuple:", list(repeated_tuple))
