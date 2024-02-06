# decimal to binary
n=int(input())
list1=[]
val=0
i=1
while i>=8:
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
    n=int(a)
    i+=1

output=""
for i in list1:
    output+=str(i)
print(output[::-1])
print(bin(99))