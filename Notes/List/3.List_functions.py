print("------------------------------------------------------------------------------------------")
print("---------------------------------Lists Function-------------------------------------------")
print("------------------------------------------------------------------------------------------")

n=[10,20,30,40]

print("---------------------------------Len Function------------------------------------------")

# len(): return the number of elements present in the list.
# syntax: len(list) 
print("Length of the list: ",len(n))


print("---------------------------------Sum Function------------------------------------------")

# sum(): sum up the numbers in the list.
# syntax: sum(iterable numbers)
print("Sum of the list",sum(n))
Sum = sum(n, 10)
print(Sum)



print("-----------------------------------Split Function------------------------------------------")
# split(): split the strings and store it to a list
# syntax: list = string.split()
lst=[]
# input the list as string
string = "Harrish P T"# input("Enter elements (Space-Separated): ")
# split the strings and store it to a list
lst = string.split()  
print('Using Split function to add string in a list is:', lst)  # append a string in a list is: ['Harrish', 'P', 'T']

print("Using Map : ")
# # input size of the list
# n = 3 # int(input("Enter the size of list : "))
# store integers in a list using map,
# split and strip functions
# lst = list(map(int, input("Enter the integer elements: ").strip().split()))[:n]
# printing the list
# print('Using Split function get the element in a list: ', lst) 


print("---------------------------------Reversed Function----------------------------------------")

# reversed(): The reversed() function returns a reverse iterator, 
# which can be converted to a list using the list() function.
n=[1, 2, 3, 4, 5]
reversed_list=list(reversed(n)) # without list function it return reversed object
print("Reversed element ",reversed_list) # [5, 4, 3, 2, 1]

# ord(): Returns an integer representing the Unicode code point of the given Unicode character.


# cmp(): This function returns 1 if the first list is “greater” than the second list


print("------------------------------------Min Function------------------------------------------")
# min(): return minimum element of a given list
# syntax: min(a, b, c, …, key=func)
# Parameters
# a, b, c, .. : similar type of data.
# key (optional): A function to customize the sort order

# Example 1:
numbers = [23,25,65,21,98]
print("Print the minimum number in the list: ",min(numbers))
print("Print the minimum number in two numbers: ",min(15,75))

# Example 2:
square = {25: 10, 8: 64, 2: 4, 3: 9, -1: 1, -2: 4}
print("Print the minimum number in dict key:", min(square))    # -2
key2 = min(square, key = lambda k: square[k]) # key parameter[-6,8,2,3,-1,-2]
print("Print the minimum number in dict value:", square[key2])    # 1

# Example 3:
languages = ["C","Python", "C++ Programming", "Java", "JavaScript",'PHP','Kotlin']
print("Print the minimum string in ascending order: ", min(languages))

# Example 4:
def func(x):
    return abs(x - 10)
print(min([6, 12, 13, -4, 5], key=func))


print("------------------------------------Max Function------------------------------------------")

# max(): return maximum element of a given list




print("---------------------------------Reduce Function------------------------------------------")
# reduce():
# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all 
# of the list elements mentioned in the sequence passed along.
# This function is defined in “functools” module.
from functools import reduce
import operator
print("Using Lambda : ")
lis = [1, 3, 5, 6, 2] 
print("The sum of the list elements is : ", end="") 
print(reduce(lambda a,b: a+b, lis)) 
print("The maximum element of the list is : ", end="") 
print(reduce(lambda a, b: a if a > b else b, lis)) 
print("-------------------------------------------------------------------")

# Using Operator Functions
# reduce() can also be combined with operator functions to achieve the similar functionality as with 
# lambda functions and makes the code more readable.

# initializing list 
print("Using Operator : ")  
# using reduce to compute sum of list 
# using operator functions 
print("The sum of the list elements is : ", end="") 
print(reduce(operator.add, lis)) 
  
# using reduce to compute product 
# using operator functions 
print("The product of list elements is : ", end="") 
print(reduce(operator.mul, lis)) 
  
# using reduce to concatenate string 
print("The concatenated product is : ", end="") 
print(reduce(operator.add, ["Hello ", "World, ", "Harrish"]))


print("-------------------------------------------------------------------")

print("Using accumalate : ")  

# reduce() vs accumulate() 
# Both reduce() and accumulate() can be used to calculate the summation of a sequence elements. 
# But there are differences in the implementation aspects in both of these.  

# reduce() is defined in “functools” module, 
# accumulate() in “itertools” module.
# reduce() stores the intermediate result and only returns the final summation value. 
# Whereas, accumulate() returns a iterator containing the intermediate results. 
# The last number of the iterator returned is summation value of the list.
# reduce(fun, seq) takes function as 1st and sequence as 2nd argument. 
# In contrast accumulate(seq, fun) takes sequence as 1st argument and function as 2nd argument.

# Syntax
# itertools.accumulate(iterable[, func]) –> accumulate object

from itertools import accumulate

iterable1 = [1, 2, 3, 4, 5] 
  
# using the itertools.accumulate()  
result_object = accumulate(iterable1,operator.mul) 
  
# printing each item from list 
print("Multiply Iterable in list using accumate: ")
for each in result_object: 
    print(each) 

# Explanation :
# The operator.mul takes two numbers and multiplies them.
# operator.mul(1, 2)
# 2
# operator.mul(2, 3)
# 6
# operator.mul(6, 4)
# 24
# operator.mul(24, 5)
# 120
iterable2 = [5, 3, 6, 2, 1, 9, 1] 
  
# using the itertools.accumulate() 
  
# Now here no need to import operator 
# as we are not using any operator 
# Try after removing it gives same result 
result = accumulate(iterable2, max) 
# printing each item from list 
for each in result: 
    print(each) 


# printing summation using accumulate() 
print("The summation of list using accumulate is :", end="") 
print(list(accumulate(lis, lambda x, y: x+y))) 

# printing summation using reduce() 
print("The summation of list using reduce is :", end="") 
print(reduce(lambda x, y: x+y, lis))  



print("---------------------------------Ord Function------------------------------------------")

# Python ord() function returns the Unicode code from a given character. This function accepts a string of unit length as an argument and returns the Unicode equivalence of the passed argument.