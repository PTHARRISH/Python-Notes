# Linear Search algorithm
# Linear search is defined as the searching algorithm
# where the list or data set is traversed from one end to find the desired value.
# Time Complexity: The worst case time complexity of linear search is o(n), where n is the size of the array.
# Space Complexity:  Linear search requires a constant amount of memory to run.
# Efficiency: Linear search is effeicient for small datasets but becomes inefficient for larger datasets. 
# In practice, linear search is often used as a subroutine in more complex algorithms.
# Implementation: Linear search can be easily implemented using a loop, 
# with each iteration comparing the target value to the current element of the array.
# 
# def search(arr, N, x):  
#     for i in range(0, N):
#         if arr[i] == x:
#             return i
#     return -1
        
# arr =[int(i) for i in input('Enter the array with comma').split(',')] 
# x = int(input('enter the number:'))
# N = len(arr)
# result = search(arr, N, x)
# if(result == -1):
#     print("Element is not present in array")
# else:
#     print("Element is present at index", result)

# Phonebook Search: Linear search can be used to search through a phonebook to find a person’s name, given their phone number. 
# Spell Checkers:  The algorithm compares each word in the document to a dictionary of correctly spelled words until a match is found.
# Finding Minimum and Maximum Values: Linear search can be used to find the minimum and maximum values in an array or list. 
# Searching through unsorted data: Linear search is useful for searching through unsorted data.


#sentinellinear search
# def sentinelLinearSearch(array, key):
#     last = array[len(array) - 1]
#     array[len(array) - 1] = key
#     i = 0
#     while array[i] != key:
#         i += 1
#     array[len(array) - 1] = last
#     if i < len(array) - 1 or last == key:
#         return i
#     else:
#         return -1
 
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# key = 5
# index = sentinelLinearSearch(array, key)
# if index == -1:
#     print(f"{key} is not found in the array: {array}")
# else:
#     print(f"{key} is found at index {index} in the array: {array}")
