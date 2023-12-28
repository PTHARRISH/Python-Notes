# Method 1 : Using Iteration.
arr=list(map(int,input().split(",")))
maxi=arr[0]
mini=arr[0]
for i in range(len(arr)):
    if arr[i]>maxi:
        maxi=arr[i]
    if arr[i]<mini:
        mini=arr[i]

print(maxi,mini)


# Method 2 : Using sort() function.
arr=[int(x) for x in input('enter the numbers: ').split(',')]
arr.sort()
print(arr[-1],arr[0])


# Using max() inbuilt function.
arr = list(eval(input("Enter the array elements: ")))
print(max(arr),min(arr))