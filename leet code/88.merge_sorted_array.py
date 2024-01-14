# 88. Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

def merge(arr1,m,arr2,n):
    i,j,k=m-1,n-1,m+n-1
    while i>=0 and j>=0:
        if arr1[i]>arr2[j]:
            arr1[k]=arr1[i]
            print(arr1[k])
            i-=1
        else:
            arr1[k]=arr2[j]
            print(arr1[k])
            j-=1
        k-=1
    if j>=0:
        arr1[:k+1]=arr2[:j+1]
    print(arr1)

merge([1,2,3,0,0,0],3,[2,5,6],3)
merge([0],0,[1],1)