S=int(input())
E=int(input())
W=int(input())
 
for i in range(S,E,W):
    celsius=int((i-32)*(5/9))
    print(str(i)+" "+str(celsius))