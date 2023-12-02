# Adding Two numbers
# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 sum = nums[i] + nums[j]
#                 if sum == target:
#                     return [i, j]
#
#
#
# n = Solution()
# nums = [2, 7, 11, 15]
# print(n.twoSum(nums, 9))

# palinedrome numbers
# def isPalindrome(self, x: int) -> bool:
#     a = str(x)[::-1]
#     if a == str(x):
#         return True
#     else:
#         return False

# class Solution:
#     def threeSum(nums, List):
#         res=[]
#         nums.sort()
#         length=len(nums)
#         for i in range(length-2):
#             if i>0 and nums[i]==nums[i-1]:
#                 continue
#             l=i+1
#             r=length-1
#             while l<r:
#                 total=nums[i]+nums[l]+nums[r]
#                 if total<0:
#                     l=l+1
#                 elif total>0:
#                     r=r-1
#                 else:
#                     res.append([nums[i],nums[l],nums[r]])
#                     while l<r and nums[l]==nums[l+1]:
#                         l=l+1
#                     while l<r and nums[r]==nums[r-1]:
#                         r=r-1
#                     l=l+1
#                     r=r-1
#         return res


# import collections
# def mindeletion(s):
#     deletion=0
#     freq=set()
#     charco=collections.Counter(s)
#     for chars,counts in charco.items():
#         while counts>0 and counts in freq:
#             counts-=1
#             deletion+=1
#         freq.add(counts)
#     return deletion

# a=input('enter: ')
# result=mindeletion(a)
# print(result)


            