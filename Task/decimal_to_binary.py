n=int(input())
list1=[]
val=0
for i in range(8):
    a=n/2
    print(a)
    b=list(str(a))[-1]
    print(b)
    if b=="5":
        c=1
        list1.append(c)
    else:
        c=0
        list1.append(c)
    n=a

print(list1)




