# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of 
# the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

# 1st method using append zeros at end
def move_zero(a):
    count=0
    n=len(a)
    for i in range(n):
        if a[i]!=0:
            a[count]=a[i]
            count+=1
        
    while count<n:
        a[count]=0
        count+=1
    return a

a=[int(i) for i in input("enter the numbers with zeros: ").split(",")]
# arr=list(map(int,input().split(' ')))
print(move_zero(a))


# 2nd method using swapping
def move_zero(nums):
    count=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[count],nums[i]=nums[i],nums[count]
            count+=1
    print(nums)
    return nums

a=[int(i) for i in input("enter the numbers with zeros: ").split(",")]
# arr=list(map(int,input().split(' ')))
print(move_zero(a))

# output:
# 1,0,0,95,0,7,4,0
# [1, 95, 7, 4, 0, 0, 0, 0]