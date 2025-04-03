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


def single_number(nums):            
        n = len(nums)
        result = [0, 0]
        index = 0

        for i in range(n):
            found = False
            for j in range(n):
                if i != j and nums[i] == nums[j]:
                    found = True
                    break
            if not found:
                result[index] = nums[i]
                index += 1
                if index == 2:
                    break

        return result

nums = list(map(int,input('enter the numbers: ').split(',')))
print(single_number(nums))