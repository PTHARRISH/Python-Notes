# interchange first and last using slicing
def interchange(arr):
    arr[0],arr[-1]=arr[-1],arr[0]
    return arr
 
# arr=[int(i) for i in input().split() ]
arr=list(map(int,input().split(' ')))
print(interchange(arr))

# interchange first and last using unpacking
def interchange(arr):
    get=arr[0],arr[-1]
    arr[-1],arr[0]=get
    return arr

arr=list(map(int,input().split(' ')))
print(interchange(arr))


# interchange first and last using swaping
def interchange(arr):
    temp=arr[0]
    arr[0]=arr[-1]
    arr[-1]=temp
    return arr

arr=list(map(int,input().split(' ')))
print(interchange(arr))

# interchange first and last using Extended iterable unpacking
def interchange(arr):
    a,*b,c=arr
    arr=[c,*b,a]
    return arr

arr=list(map(int,input().split(' ')))
print(interchange(arr))