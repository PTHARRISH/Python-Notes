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



# Binary search

# Divide the search space into two halves by finding the middle index “mid”. 
# Compare the middle element of the search space with the key. 
# If the key is found at middle element, the process is terminated.
# If the key is not found at middle element, choose which half will be used as the next search space.
# If the key is smaller than the middle element, then the left side is used for next search.
# If the key is larger than the middle element, then the right side is used for next search.
# This process is continued until the key is found or the total search space is exhausted.

# Python3 code to implement iterative Binary search
# It returns location of x in given array arr


# def binarySearch(arr, l, r, x):
# 	while l<=r:
# 		mid=l+(r-1)//2
# 		if arr[mid]==x:
# 			return mid
# 		elif arr[mid]<x:
# 			l=mid+1
# 		else:
# 			r=mid-1
# 	return -1
# 	# If we reach here, then the element
# 	# was not present
# arr = [int(i) for i in input('enter array: ').split(",")]
# x = 10
# result = binarySearch(arr, 0, len(arr)-1, x)
# if result != -1:
# 	print("Element is present at index", result)
# else:
# 	print("Element is not present in array")


# Implementation of Recursive  Binary Search Algorithm:

# def binary(arr,l,r,x):
# 	if r>=l:
# 		mid=l+(r-1)//2
# 		if arr[mid]==x:
# 			return mid
# 		elif arr[mid]>x:
# 			return binary(arr,l,mid-1,x)
# 		else:
# 			return binary(arr,mid+1,r,x)
# 	return -1
# arr = [int(i) for i in input('enter array: ').split(",")]
# x = 10
# result = binary(arr, 0, len(arr)-1, x)
# if result != -1:
# 	print("Element is present at index", result)
# else:
# 	print("Element is not present in array")

# Time Complexity: 
# Best Case: O(1)
# Average Case: O(log N)
# Worst Case: O(log N)
# Auxiliary Space: O(1), If the recursive call stack is considered then the auxiliary space will be O(logN).

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class Sll:
#     def __init__(self):
#         self.head=None
    
#     def tranversal(self):
#         if self.head is None:
#             print("linked list is empty")
#         else:
#             a=self.head
#             while a is not None:
#                 print(a.data,end=" ")
#                 a=a.next

# n1=Node(5)
# sll=Sll()
# sll.head=n1
# n2=Node(10)
# n1.next=n2
# n3=Node(15)
# n2.next=n3
# n4=Node(20)
# n3.next=n4
# sll.tranversal()

# def search(arr,v):
#     l=len(arr)
#     for i in range(l):
#         if arr[i]==v:
#             return i
#     else:
#         return -1

# def search(arr,l,r,v):
#     while l<=r:
#         mid=l+(r-1)//2
#         if arr[mid]==v:
#             return mid
#         elif arr[mid]<r:
#             l=mid+1
#         else:
#             r=mid-1
#     return -1


# def search(arr,l,r,v):
#     if l<=r:
#         mid=l+(r-1)//2
#         if arr[mid]==v:
#             return mid
#         elif arr[mid]>r:
#             return search(arr,l,mid-1,v)
#         else:
#             return search(arr,mid+1,r,v)
#     return -1



# arr=[int(x)for x in input('array').split(",")]
# v=int(input())
# result=search(arr,0,len(arr),v)
# print(result)

# def partition(data,l,r):
#     pivot=data[r]
#     i=l-1#0
#     for j in range(l,r):
#         if data[j]<=pivot:
#             i=i+1
#             (data[i],data[j])=(data[j],data[i])
#     (data[i+1],data[r])=(data[r],data[i+1])
#     return i+1



# def quickSort(data,l,r):
#     if l<r:
#         pi=partition(data,l,r)
#         quickSort(data,l,pi-1)
#         quickSort(data,pi+1,r)



# data=[1,7,4,1,10,9,-2]
# print("Unsorted Array")
# print(data) 
# r=len(data)-1
# print(r)
# quickSort(data,0,r)
# print('Sorted Array in Ascending Order:')
# print(data)


# Approach 2: Quicksort using list comprehension

# def quicksort(arr):
# 	if len(arr) <= 1:
# 		return arr
# 	else:
# 		pivot = arr[0]
# 		left = [x for x in arr[1:] if x < pivot]
# 		right = [x for x in arr[1:] if x >= pivot]
# 		return quicksort(left) + [pivot] + quicksort(right)

# # Example usage
# arr = [1, 7, 4, 1, 10, 9, -2]
# sorted_arr = quicksort(arr)
# print("Sorted Array in Ascending Order:")
# print(sorted_arr)


def insertionSort(arr):
	n = len(arr) # Get the length of the array
	
	if n <= 1:
		return # If the array has 0 or 1 element, it is already sorted, so return

	for i in range(1, n): # Iterate over the array starting from the second element
		key = arr[i] # Store the current element as the key to be inserted in the right position
		j = i-1
		while j >= 0 and key < arr[j]: # Move elements greater than key one position ahead
			arr[j+1] = arr[j] # Shift elements to the right
			j -= 1
		arr[j+1] = key # Insert the key in the correct position

# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)

