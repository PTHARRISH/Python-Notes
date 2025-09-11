# Array
# Arrays are not native data structures in Python.
# Instead, we use list, which are similar but more flexible.

# However, there are models available in Python
# for creating more efficient arrays with a specific data
# type, mainly for numeric data type.

# We can use numpy module and array module to create an array data structure in Python.

# They store elements as contiguous block of memory without pointers,
# reducing memory overhead.

# array objects can only store elements of same data type.

# The simple examples of array data structures:
# collections of books,
# clothes in wardrobe or
# pens in your pen stand.

# Real world Examples of Array
# box of macarons.

# So this is very similar to the array data structure.

# If you look at this box very carefully,
# we can easily see what are the properties of this box.

# First is it's a box of macarons which holds macarons in it.

# This means that this box is produced for macarons.

# You cannot store,
# for example,

# 1. this cream puff into this box because it's not going to fit in.

# 2. The next property is that all macarons in this box are next to each other.

# 3. There is no gap between them, which means that they are contiguous.

# 4.And the next property is that each macaroon here can be identified
# uniquely based on their location.

# So this is the first macaroon.This is the second.This is the third.
# And it continues like this.

# So based on their location, we can identify them.

# So these are the common properties of this box and can be seen very easily.

# If you compare this box of macarons with the array data structure,
# we can see that they are very similar.

# So a typical array structure looks like this.

# You can easily see that the appearance of the macarons box and
# array data structure somehow looks each other.

## properties of this array

# The first property is an array can store data of specified type.

# This means that when we create an array of integers,
# we cannot store string values in the array.

# As you see, in case of macaron box,
# we cannot store any other suite which will not fit in this box.

# So here the data type is macaroon. We cannot store this creampuff in this array.

# The data type is integer, so we cannot store the string.

# Now the next property is elements of array are located in a contiguous location in memory.

# This means that the elements are located next to each other.

# There is no gap between them, so they have to be located contiguously in the memory.

# Now the next property is each element of array has a unique index.

# For example, the index of ten over here is going to be two and the index of four is going to be zero.

# And keep in mind that the first element's index starts from zero and increase sequentially.

# So these are the main properties of the array data structure and we have compared it with the real life

# example to understand it very well.

# why do we need array data structure?

# So consider a situation where we need to create three integer variables.
# So if we create them, we can name them like this.

# Number one, Number two, Number three.

# Now, this is very simple because we have to store just three integer numbers.

# Now let's assume we have to store 500 integer numbers.

# Are we going to use 500 variables? Of course not.

# To handle such situations, all programming languages provide a concept called array.

# An array is a data structure which can store collection of elements of the same type.

# So array is used to store a collection of data, but it is more often useful to think of array as a

# collection of variables of the same type.

# So instead of declaring individual 500 variables, we are just going to create an array and we are going

# to access the elements of array as we need them.


# What are arrays?
# An array is a container which can hold a fix number of items
# and these items should be of the same type.
# Each item stored in an array is called an element
# and they can be of any type including integers, floats, strings, etc.

# These elements are stored at contiguous memory location.
# Each location of an element in an array has a numerical index starting from 0.
# These indices are used to identify and access the elements.
