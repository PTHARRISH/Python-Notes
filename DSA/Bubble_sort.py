def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            print(i,j)
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                print(arr)
    return arr

arr=list(map(int,input("enter the numbers: ").split(",")))
print(bubble(arr))