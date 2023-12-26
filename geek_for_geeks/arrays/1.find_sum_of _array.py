# Find Sum of Array
# 1.Using Brute force
def sum_of_arr(arr):
    sum=0
    for i in arr:
        sum+=i
    print('The sum of the array loop is ',sum)

n=list(map(int,input('Enter the numbers: ').split(',')))
sum_of_arr(n)
# Time complexity: O(n)


# 2.Inbuilt Function
sum_of_arr=sum(n)
print('The sum of the array inbuilt function is ',sum_of_arr)
# Time complexity: O(n) 


# 3.Using reduce method
# Using the reduce method. Array.
# reduce() method is used to iterate over the array and get the summarized result from all elements of array.
from functools import reduce
a=reduce(lambda a,b:a+b,n)
print('The sum of the array using reduce method is ',a)
# Time complexity : O(n)

# 4.Using Enumerate
sum=0 
for i,j in enumerate(n):
    sum+=j
print('The sum of the array enumerate is ',sum)

# 5.Using Divide and Conquer method
def sum_of_array(arr,low,high):
    if low==high:
        return arr[low]
    mid=(low+high)//2
    left_sum=sum_of_array(arr,low,mid)
    right_sum=sum_of_array(arr,mid+1,high)
    return left_sum+right_sum

arr=list(map(int,input('Enter the numbers: ').split(',')))
print("The sum of the array is ",sum_of_array(arr,0,len(arr)-1))

# 6.Using counter method.
from collections import Counter

arr = [12, 3, 4, 15]
c = Counter(arr)
sum = 0
for key, value in c.items():
    sum += key * value

print("Sum of the array is", sum)
