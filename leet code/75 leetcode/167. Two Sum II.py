def twosum_sorted(nums,target):
    lp = 0
    rp = len(nums)-1
    while lp<rp:
        s = nums[lp]+nums[rp]
        if s==target:
            return [lp+1,rp+1]
        elif s<target:
            lp+=1
        else:
            rp-=1


data = sorted(list(map(int,input('enter the number: ').split(','))))
target = int(input('target: '))
print(twosum_sorted(data,target))

# Output:
# enter the number: 2,7,11,15
# target: 9
# [1, 2]