def countHillValley(nums):
    n = len(nums)
    i = 1
    count = 0
    while i < n - 1:
        left = i - 1
        while left >= 0 and nums[left] == nums[i]:
            left -= 1
        right = i + 1
        while right < n and nums[right] == nums[i]:
            right += 1
        if left >= 0 and right < n:
            if nums[left] < nums[i] and nums[right] < nums[i]:
                count += 1
            elif nums[left] > nums[i] and nums[right] > nums[i]:
                count += 1
        i = right
    return count


arr = list(map(int, input("enter the array: ").split(",")))
print(countHillValley(arr))
