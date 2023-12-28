# Method 1 : Using two loops
import math
arr = list(eval(input("Enter the array elements: ")))
first=math.inf
second=math.inf

for i in range(0,len(arr)):
    if arr[i]<first:
        first=arr[i]
for j in range(0,len(arr)):
    if arr[j]!=first and arr[j]<second:
        second=arr[j]
print(second)


# Method 2 : Using loop
arr=list(map(int,input('Enter the array elements: ').split(",")))
first=second=math.inf
for i in range(0,len(arr)):
    if arr[i]<first:
        second=first
        first=arr[i]
    elif arr[i]!=first and second>arr[i]:
        second=arr[i]
print(second)


#  Method 3 : Using sort function
arr = [10, 13, 17, 11, 34, 21]
arr.sort()
print("second smallest element in array:",arr[1])


print("second smallest element in array:")
arr = [10, 89, 9, 56, 4, 80, 8]
arr.sort()
arr.remove(arr[0])
print(arr[0])


