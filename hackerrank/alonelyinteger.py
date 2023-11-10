def lonelyinteger(a):
    b=sorted(a)
    if len(b)==1:
        return b[0]
    else:
        for i in range(len(b)): 
            count=0
            for j in range(len(b)):
                if b[i]==b[j]:
                    count+=1
            if count==1:
                return b[i]
          
a=list(map(int,input().split()))
print(lonelyinteger(a))