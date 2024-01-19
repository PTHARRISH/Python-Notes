# Method 1 : Using Iteration.
arr=list(map(int,input().split(",")))
maximum=arr[0]
for i in range(len(arr)):
    if arr[i]>maximum:
        maximum=arr[i]
print(maximum)


# Method 2 : Using sort() function.
arr=[int(x) for x in input('enter the numbers: ').split(',')]
arr.sort()
print(arr[-1])


# Using max() inbuilt function.
arr = list(eval(input("Enter the array elements: ")))
print(max(arr))