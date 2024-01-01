print("------------------------------------------------------------------------------------------")
print("---------------------------------Lists Function-------------------------------------------")
print("------------------------------------------------------------------------------------------")

n=[10,20,30,40]

# len(): return the number of elements present in the list.
# syntax: len(list) 
print("Length of the list: ",len(n))


# sum(): sum up the numbers in the list.
# syntax: sum(iterable numbers)
print("Sum of the list",sum(n))


# split(): split the strings and store it to a list
# syntax: list = string.split()
# lst=[]
# # input the list as string
# string = input("Enter elements (Space-Separated): ")
# # split the strings and store it to a list
# lst = string.split()  
# print('The list is:', lst)  


# # input size of the list
# n = int(input("Enter the size of list : "))
# # store integers in a list using map,
# # split and strip functions
# lst = list(map(int, input("Enter the integer\
# elements:").strip().split()))[:n]

# # printing the list
# print('The list is:', lst) 



# reversed(): The reversed() function returns a reverse iterator, 
# which can be converted to a list using the list() function.
n=[1, 2, 3, 4, 5]
reversed_list=list(reversed(n)) # without list function it return reversed object
print("Reversed element ",reversed_list) # [5, 4, 3, 2, 1]


print("---------------------------------Reduce Function------------------------------------------")
# reduce():
# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all 
# of the list elements mentioned in the sequence passed along.
# This function is defined in “functools” module.
import functools 
lis = [1, 3, 5, 6, 2] 
print("The sum of the list elements is : ", end="") 
print(functools.reduce(lambda a, b: a+b, lis)) 





# ord(): Returns an integer representing the Unicode code point of the given Unicode character.


# cmp(): This function returns 1 if the first list is “greater” than the second list


print("---------------------------------Reduce Function------------------------------------------")
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



# max(): return maximum element of a given list
