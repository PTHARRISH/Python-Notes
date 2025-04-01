# 137. Single Number II
def single_number(nums):
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 1
        elif i in d and d[i]!=2:
            d[i]+=1
        else:
            del d[i]
    return list(d.keys())[0]
nums = list(map(int,input('enter the numbers: ').split(',')))
print(single_number(nums))