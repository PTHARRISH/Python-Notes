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


