# Method 1 : Using Iteration.
arr=list(map(int,input().split(",")))
minimum=arr[0]
for i in range(len(arr)):
    if arr[i]<minimum:
        minimum=arr[i]
print(minimum)

# Method 2 : Using sort() function.
arr=[int(x) for x in input('enter the numbers: ').split(',')]
arr.sort()
print(arr[0])


# Using max() inbuilt function.
arr = list(eval(input("Enter the array elements: ")))
print(min(arr))