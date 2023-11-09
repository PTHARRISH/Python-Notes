def find_duplicate(arr):
    temp=set()
    duplicate=set()
    for i in arr:
        if i not in temp:
            temp.add(i)
        else:
            duplicate.add(i)
    if duplicate:
        return sorted(list(duplicate))
    return [-1]


arr=list(map(int,input(' enter the array element').strip().split()))
result=find_duplicate(arr)
for i in result:
    print(i,end=' ')

