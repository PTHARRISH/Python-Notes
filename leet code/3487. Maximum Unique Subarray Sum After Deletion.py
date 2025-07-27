# 3487. Maximum Unique Subarray Sum After Deletion
def maxSum(nums):
    data = set()
    if len(nums) == 1:
        return nums[0]
    for i in nums:
        if i not in data and i > 0:
            data.add(i)
    if i < 0:
        data.add(max(nums))
    total_data = sum(data)
    return total_data


arr = list(map(int, input("Enter the array:").split(",")))
print(maxSum(arr))
