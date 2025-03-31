# 136. Single Number
def single_number(nums):
    data = {}
    for i in nums:
        if i not in data:
            data[i] = 1
        else:
            del data[i]
    return list(data.keys())[0]

nums = list(map(int,input('enter the numbers: ').split(',')))
print(single_number(nums))