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