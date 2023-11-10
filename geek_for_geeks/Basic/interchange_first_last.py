def interchange(arr):
    arr[0],arr[-1]=arr[-1],arr[0]
    return arr
 



# arr=[int(i) for i in input().split() ]
arr=list(map(int,input().split(' ')))
print(interchange(arr))

