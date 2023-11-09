def print2largest(arr, n):
	arr1=sorted(list(set(arr)))
	if len(arr1)>1:
		return arr1[-2]
	return -1

def print2largest(arr, n):
	list2=[x for x in arr if x<max(arr)]
	return max(list2)

# second largest element without sorting function	
def secondlargest(arr,n):
	a=max(arr)
	arr.remove(a)
	print(max(arr))

secondlargest([1,0,8,92,100],5)
