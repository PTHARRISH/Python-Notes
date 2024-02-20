def binarysearch(arr,target):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1


arr=[int(x) for x in input("Enter the value: ").split(",")]
target=int(input("enter the target value: "))
print(binarysearch(arr,target))


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
