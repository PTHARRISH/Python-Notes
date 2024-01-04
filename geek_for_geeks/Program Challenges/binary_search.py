def binarysearch(arr, k):
		# code here
        n=len(arr)
        for i in range(0,n):
            if arr[i]== k:
                return i
        return -1 

arr=[int(i) for i in input("Enter the array: ").split(",")] # 1,21,22,89,100,210
s=int(input("Target: ")) # 210
print(binarysearch(arr,s)) # 5

