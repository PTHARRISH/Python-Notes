# Array Rotation
def array_rotation(arr,n,d):
    temp=[]
    i=0
    while i<d:
        temp.append(arr[i])
        i+=1
    i=0
    while d<n:
        arr[i]=arr[d]
        i+=1
        d+=1
    arr[:]=arr[:i]+temp
    return arr

arr=list(map(int,input('enter the array: ').split(',')))
size=len(arr)
d=int(input())
print(array_rotation(arr,size,d))

# Time complexity: O(n)
# output: [4, 5, 6, 1, 2, 3]
def rotation(arr,n,d):
    d=d%n
    arr[:]=arr[d:]+arr[:d]
    return arr


arr=list(map(int,input('enter the array: ').split(',')))
size=len(arr)
d=int(input())
print(rotation(arr,size,d))
