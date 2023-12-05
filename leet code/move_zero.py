# move zeros at the end
def move_zero(a):
    count=0
    n=len(a)
    for i in range(n):
        if a[i]!=0:
            a[count]=a[i]
            count+=1
        
    while count<n:
        a[count]=0
        count+=1
    return a


a=[int(i) for i in input().split(",")]
# arr=list(map(int,input().split(' ')))
print(move_zero(a))
