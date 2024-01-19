# 80. Remove Duplicates from Sorted Array II

# Given an integer array nums sorted in non-decreasing order, 
# remove some duplicates in-place such that each unique element appears at most twice. 
# The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, 
# you must instead have the result be placed in the first part of the array nums. 
# More formally, if there are k elements after removing the duplicates, 
# then the first k elements of nums should hold the final result. 
# It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. 
# You must do this by modifying the input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 
def removeDuplicates(nums):
    l,r=0,0 # l-> left pointer , r-> right pointer 
    while r<len(nums): # r=0 | r=3 | r=5
        count=1 # count the duplicate 
        while r+1<len(nums) and nums[r]==nums[r+1]:  # [0]==[1] True [1]==[2] True [2]!=[3] False | 4<6 and [3]==[4] True, 5<6 and [4]==[5] False | False
        # while r+1 < len(nums) right pointer will be with in the length and it will equal to right== right+1  
            r+=1 # r=1, r=2 [1,1,1] | r=4 
            count+=1 # count=2 , count=3 | count=2
        for i in range(min(2,count)): # min(2 ,3) | min(2,2)
            nums[l]=nums[r] # nums[0]=nums[2] # nums[0]=1 | nums[1]= nums[4] # nums[1]=2
            l+=1 # l=1 | l=2
        r+=1 # r=3 | r=5
    return l

nums =[1,1,1,2,2,3]
print(removeDuplicates(nums))


def removeDuplicates(nums):
    index=1
    count=1
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]: # [1]==[0] | [2]==[1] | [3]==[2] False |
            count+=1 # 2 | 3 
        else:
            count=1 # | 1
        if count<=2: # 2==2 | False |1<2
            nums[index]=nums[i] # nums[1]=nums[0] # 1 | nums[2]=nums[3]
            print(nums[index],nums[i])
            index+=1 # 2
    return index
    

nums =[1,1,1,2,2,3]
print(removeDuplicates(nums)) # [1, 1, 2, 2, 3, 3]