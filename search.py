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


