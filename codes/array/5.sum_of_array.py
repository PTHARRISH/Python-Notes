arr=[int(x) for x in input('enter the numbers: ').split(',')]
# x,*y=input().split(',')
# print(type(y))
# Method 1 : Using Iteration
sum1=0
for i in arr:
    sum1+=i
print("Using iteration method: ",sum1)

# Method 2 : Using recursion

def sumofarr(arr,n):
    if n==0:
        return 0
    else:
        return arr[n-1]+sumofarr(arr,n-1)

print("Using recursion method: ",sumofarr(arr,len(arr)))

# Method 3 : Using inbuilt Function

print("Using Inbuilt function: ",sum(arr))