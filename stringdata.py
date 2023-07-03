# String
# A string is a data structure in Python that represents a sequence of characters.
# It is an immutable data type, meaning that once you have created a string, you cannot change it.
# Strings are used widely in many different applications, such as storing and manipulating text data,
# representing names, addresses, and other types of data that can be represented as text.

# Example:
# "Geeksforgeeks" or 'Geeksforgeeks'

# Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

# print("A Computer Science portal for geeks") # A Computer Science portal for geeks

# Creating a String in Python
# Strings in Python can be created using single quotes or double quotes or even triple quotes.

# Python Program for Creation of String with single Quotes
# String1 = 'Welcome to the Geeks World'
# print("String with the use of Single Quotes: ") # String with the use of Single Quotes:
# print(String1) # Welcome to the Geeks World

# Creating a String with double Quotes
# String1 = "I'm a Geek" # double quotes inside single quotes can be used
# print("\nString with the use of Double Quotes: ") # string escape sequences can be used inside double quotes
# print(String1)

# Creating a String with triple Quotes
# String1 = '''I'm a Geek and I live in a world of "Geeks"''' # It is also called as multiline comments
# print("\nString with the use of Triple Quotes: ")
# print(String1)

# Creating String with triple Quotes allows multiple lines
# String1 = '''Geeks
# 			For
# 			Life'''
# print("\nCreating a multiline String: ")
# print(String1)# print exactly like this format spaces may differs


# Accessing characters in Python String
# In Python, individual characters of a String can be accessed by using the method of Indexing.
# Indexing allows negative address references to access characters from the back of the String,
# e.g. -1 refers to the last character, -2 refers to the second last character, and so on.
# While accessing an index out of the range will cause an IndexError.
# Only Integers are allowed to be passed as an index, float or other types that will cause a TypeError.

# Python Program to Access characters of String
# String1 = "GeeksForGeeks"
# print("Initial String: ")
# print(String1) #GeeksForGeeks

# Printing First character
# print("\nFirst character of String is: ")
# print(String1[0]) #G

# Printing Last character
# print("\nLast character of String is: ")
# print(String1[-1]) #s

# Reversing a Python String
# With Accessing Characters from a string,
# we can also reverse them. We can Reverse a string by writing [::-1] and the string will be reversed.

# Program to reverse a string
# gfg = "geeksforgeeks"
# print(gfg[::-1]) #skeegrofskeeg

# We can also reverse a string by using built-in join and reversed function.
# Program to reverse a string
# gfg = "geeksforgeeks"

# Reverse the string using reversed and join function
# gfg = "".join(reversed(gfg))
#
# print(gfg) #skeegrofskeeg


# String Slicing
# To access a range of characters in the String, the method of slicing is used.
# Slicing in a String is done by using a Slicing operator (colon).

# Python Program to demonstrate String slicing
# Creating a String
# String1 = "GeeksForGeeks"
# print("Initial String: ")
# print(String1) #GeeksForGeeks

# Printing 3rd to 12th character
# print("\nSlicing characters from 3-12: ")
# print(String1[3:12]) #ksForGeek

# Printing characters between 3rd and 2nd last character
# print("\nSlicing characters between " +
# 	"3rd and 2nd last character: ")
# print(String1[3:-2]) #ksForGee


# Deleting/Updating from a String
# In Python, the Updation or deletion of characters from a String is not allowed.
# This will cause an error because item assignment or item deletion from a String is not supported.
# Although deletion of the entire String is possible with the use of a built-in del keyword.(del str1)
# This is because Strings are immutable, hence elements of a String cannot be changed once it has been assigned.
# Only new strings can be reassigned to the same name.

# Updation of a character:
# Python Program to Update character of a String
# String1 = "Hello, I'm a Geek"
# print("Initial String: ")
# print(String1)

# Updating a character of the String
# As python strings are immutable, they don't support item updation directly
# there are following two ways

# 1
# list1 = list(String1) #Hello, I'm a Geek #convert string into list and update value
# list1[2] = 'p'
# String2 = ''.join(list1)
# print("\nUpdating character at 2nd Index: ")
# print(String2)#Heplo,I'm a Geek

# now the final output is string format,
# because we store a list value using join string function the value will be store in a new string

# 2
# String3 = String1[0:2] + 'p' + String1[3:] # split and concatinate string
# print(String3)#Heplo, I'm a Geek

# Python Program to Update entire String
# String1 = "Hello, I'm a Geek"
# print("Initial String: ")
# print(String1) # Hello, I'm a Geek

# Updating a String
# String1 = "Welcome to the Geek World"
# print("\nUpdated String: ")
# print(String1) #Welcome to the Geek World #it wil reassign a value to the variable


# Deletion of a character:
# Python Program to Delete characters from a String
# String1 = "Hello, I'm a Geek"
# print("Initial String: ")
# print(String1)

# Deleting a character of the String
# String2 = String1[0:2] + String1[3:]
# print("\nDeleting character at 2nd Index: ")
# print(String2) #Helo, I'm a Geek


# Deleting Entire String:
# Deletion of the entire string is possible with the use of del keyword.
# Further, if we try to print the string,
# this will produce an error because String is deleted and is unavailable to be printed.

# Python Program to Delete entire String
# String1 = "Hello, I'm a Geek"
# print("Initial String: ")
# print(String1) # Hello, I'm a Geek

# Deleting a String with the use of del
# del String1
# print("\nDeleting entire String: ")
# print(String1) # Now it Show a NameError: name 'String1' is not defined


# Escape Sequencing in Python
# While printing Strings with single and double quotes in it causes SyntaxError,
# because String already contains Single and Double Quotes and hence cannot be printed with the use of either of these.
# Hence, to print such a String either Triple Quotes are used or Escape sequences are used to print such Strings.

# Escape sequences start with a backslash and can be interpreted differently.
# If single quotes are used to represent a string,
# then all the single quotes present in the string must be escaped and same is done for Double Quotes.

# Python Program for
# Escape Sequencing
# of String

# Initial String
# String1 = '''I'm a "Geek"'''
# print("Initial String with use of Triple Quotes: ")
# print(String1)

# Escaping Single Quote
# String1 = 'I\'m a "Geek"'
# print("\nEscaping Single Quote: ")
# print(String1) # I'm a "Geek"

# Escaping Double Quotes
# String1 = "I'm a \"Geek\""
# print("\nEscaping Double Quotes: ")
# print(String1)  # I'm a "Geek"

# Printing Paths with the use of Escape Sequences
# String1 = "C:\\Python\\Geeks\\"
# print("\nEscaping Backslashes: ")
# print(String1)  # C:\Python\Geeks\

# Printing Paths with the use of Tab
# String1 = "Hi\tGeeks"
# print("\nTab: ")
# print(String1)  # Hi    Geeks

# Printing Paths with the use of New Line
# String1 = "Python\nGeeks"
# print("\nNew Line: ")
# print(String1)
# python
# Geeks

# To ignore the escape sequences in a String, r or R is used,
# this implies that the string is a raw string and escape sequences inside it are to be ignored.

# Printing hello in octal
# String1 = "\110\145\154\154\157"
# print("\nPrinting in Octal with the use of Escape Sequences: ")
# print(String1)  # Hello

# Using raw String to ignore Escape Sequences
# String1 = r"This is \110\145\154\154\157"
# print("\nPrinting Raw String in Octal Format: ")
# print(String1)  # This is \110\145\154\154\157

# Printing Geeks in HEX
# String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
# print("\nPrinting in HEX with the use of Escape Sequences: ")
# print(String1)  # This is Geeks in HEX

# Using raw String to ignore Escape Sequences
# String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
# print("\nPrinting Raw String in HEX Format: ")
# print(String1)  # This is \x47\x65\x65\x6b\x73 in \x48\x45\x58


# Formatting of Strings
# Strings in Python can be formatted with the use of format() method.
# which is a very versatile and powerful tool for formatting Strings.
# Format method in String contains curly braces {} as placeholders,
# which can hold arguments according to position or keyword to specify the order.

# format()
# Python string format() function has been introduced for handling complex string formatting more efficiently.
# Sometimes we want to make generalized print statements .
# In that case instead of writing print statement every time we use the concept of formatting.

# txt = "I have {an:.2f} Rupees!"
# print(txt.format(an=4))

# This method of the built-in string class provides functionality for complex variable substitutions and value
# formatting. This new formatting technique is regarded as more elegant. The general syntax of format() method is
# string.format(var1, var2,…). Here we will try to understand how to Format A String That Contains Curly Braces In
# Python.

# A simple demonstration of Python String format() Method Formatters work by putting in one or more replacement
# fields and placeholders defined by a pair of curly braces { } into a string and calling the str.format(). The value
# we wish to put into the placeholders and concatenate with the string passed as parameters into the format function.

# Syntax of string format() function
# Syntax: { }.format(value)

# Parameters:
# value : Can be an integer, floating point numeric constant, string, characters or even variables.
# Returntype: Returns a formatted string with the value passed as parameter in the placeholder position.

# Using a Single Formatter
# In this example, we will use the string bracket notation program to demonstrate the str.format() method.

# using format option in a simple string
# print("{}, A computer science portal for geeks."
#       .format("GeeksforGeeks"))  # GeeksforGeeks , A computer science portal for geeks.

# using format option for a value stored in a variable
# str = "This article is written in {}"
# print(str.format("Python"))  # This article is written in Python

# formatting a string using a numeric constant
# print("Hello, I am {} years old !".format(18))  # Hello, I am 18  years old !


# String format() with multiple placeholders
# Multiple pairs of curly braces can be used while formatting the string in Python.
# Let’s say another variable substitution is needed in the sentence, which can be done by adding a second
# pair of curly braces and passing a second value into the method. Python will replace the placeholders with values
# in order.

# Syntax : { } { } .format(value1, value2)

# Parameters :  (value1, value2) : Can be integers, floating point numeric constants, strings, characters and even
# variables. Only difference is, the number of values passed as parameters in format() method must be equal to the
# number of placeholders created in the string.

# Errors and Exceptions : IndexError : Occurs when string has an extra placeholder, and we didn’t pass any value for
# it in the format() method. Python usually assigns the placeholders with default index in order like 0, 1, 2,
# 3…. to access the values passed as parameters. So when it encounters a placeholder whose index doesn’t have any
# value passed inside as parameter, it throws IndexError.

# Python program using multiple placeholders to demonstrate str.format() method.
# Multiple placeholders in format() function
# my_string = "{}, is a {} science portal for {}"
# print(my_string.format("GeeksforGeeks", "computer", "geeks"))  # GeeksforGeeks, is a computer science portal for geeks

# different datatypes can be used in formatting
# print("Hi ! My name is {} and I am {} years old"
#       .format("User", 19))  # Hi ! My name is User and I am 19 years old

# The values passed as parameters
# are replaced in order of their entry
# print("This is {} {} {} {}"
#       .format("one", "two", "three", "four"))  # This is one two three four


# String format() IndexError
# Python program demonstrating Index error number of placeholders is four but there are only three values passed.
# parameters in format function.
# my_string = "{}, is a {} {} science portal for {}"
# print(my_string.format("GeeksforGeeks", "computer", "geeks"))  #IndexError: Replacement index 3 out of range for positional args tuple

# Formatting Strings using Escape Sequences
# You can use two or more specially designated characters within a string to format a string or perform a command.
# These characters are called escape sequences. An Escape sequence in Python starts with a backslash (\).
# For example, \n is an escape sequence in which the common meaning of the letter n is literally escaped
# and given an alternative meaning – a new line.

# \n -Breaks the string into a new line
# print('I designed this rhyme to explain in due time\nAll I know')

# \t -Adds a horizontal tab
# print('Time is a \tvaluable thing')

# \\ -Prints a backslash
# print('Watch it fly by\\as the pendulum swings')

# \’ -Prints a single quote
# print('It doesn\'t even matter how hard you try')

# \”  -Prints a double quote
# print('It is so\"unreal\"')

# \a -makes a sound like a bell
# print('\a')


# Formatters with Positional and Keyword Arguments
# When placeholders { } are empty, Python will replace the values
# passed through str.format() in order. The values that exist within the str.format() method are essentially tuple
# data types and each individual value contained in the tuple can be called by its index number, which starts with
# the index number 0. These index numbers can be passed into the curly braces that serve as the placeholders in the
# original string.

# Syntax : {0} {1}.format(positional_argument, keyword_argument)
# Parameters : (positional_argument, keyword_argument)

# Positional_argument can be integers, floating point numeric constants, strings, characters and even variables.
# Keyword_argument is essentially a variable storing some value, which is passed as parameter.

