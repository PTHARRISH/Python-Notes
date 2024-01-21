# print the first half in ascending order and second half in descending order

def printorder(arr,n):
    arr.sort()
    i=0
    while i<n//2:
        print(arr[i], end=" ")
        i+=1
    j=n-1
    while j>=n//2:
        print(arr[j], end=" ")
        j-=1

printorder([1,2,3,4,6,5],6)


# using while loop and slicing method
def order(arr,n):
    arr.sort()
    i=n-1 # 6 5 4 
    j=n//2 # 3 4 5
    arr1=[]
    arr1[:]=arr[:n//2]
    while i>=n//2:
        arr1.append(arr[i])
        i-=1
    print(arr1) 

order([1,2,3,4,5,6],6)

