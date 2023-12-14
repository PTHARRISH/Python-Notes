#Move all zeroes to end of array
def zeroatend(arr,n):
    list1=[]
    for i in arr:
        if i==0:
            continue
        else:
            list1.append(i)
    m=len(list1)
    print(m,n)
    while n>=m:
        list1.append(0)
        m+=1
    print(list1)
arr=[3,5,0,0,4,0,0]
zeroatend(arr,len(arr))