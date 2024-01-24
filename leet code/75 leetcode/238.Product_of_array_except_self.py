# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all 
# the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

def productExceptSelf(nums):
        n=len(nums)
        left= [0]*n
        right=[0]*n
        answer=[0]*n
        
        #Compute left products
        left[0]=1
        for i in range(1, n):
            left[i]=nums[i-1]*left[i-1]
        #compute right products
        right[n-1]=1
        for i in range(n-2, -1,-1):
            right[i]=nums[i+1]*right[i+1]
        
        #calculate answer
        for i in range(n):
            answer[i]=left[i]*right[i]
            
        return answer

nums=[-1,1,0,-3,3]
print(productExceptSelf(nums))
# [0, 0, 9, 0, 0]


def productExceptSelf(nums):
    n=len(nums)
    final=[1]*n
    pre=1
    suf=1
    for i in range(n):
        final[i]=pre
        pre=pre*nums[i]
    for j in range(n-1,-1,-1):
        final[j]=suf*final[j]
        suf=suf*nums[j]
    return final

nums =[1,2,3,4]
print(productExceptSelf(nums))
# [24, 12, 8, 6]