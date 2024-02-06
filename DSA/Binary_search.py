def binarysearch(arr,target):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1


arr=[int(x) for x in input("Enter the value: ").split(",")]
target=int(input("enter the target value: "))
print(binarysearch(arr,target))