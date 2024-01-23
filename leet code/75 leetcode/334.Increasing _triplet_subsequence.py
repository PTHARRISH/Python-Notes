# 334. Increasing Triplet Subsequence
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
# such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

 
def increasingTriplet(nums):
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

nums =[1,2,3,4,5]
print(increasingTriplet(nums))

def increasingTriplet(nums):
        n=len(nums)
        n1=float('inf')
        n2=float('inf')
        for i in range(n):
            if nums[i]>n2:
                return True
            if nums[i]<n1 :
                n1=nums[i]
            elif nums[i]>n1 and nums[i]<n2:
                n2=nums[i]
        return False

nums =[2,1,5,0,4,6]
print(increasingTriplet(nums))