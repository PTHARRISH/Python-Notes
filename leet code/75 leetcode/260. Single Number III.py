# 260. Single Number III
def single_number(nums):
    data = {}
    for i in nums:
        if i not in data:
            data[i]=1
        else:
            del data[i]
    return list(data.keys())[:2]
    
def single_number(nums):
    nums.sort()
    data = []
    for i in nums:
        s = nums.count(i)
        if s!=2:
            data.append(i)
        if len(data)==2:
            return data
            

nums = list(map(int,input('enter the numbers: ').split(',')))
print(single_number(nums))