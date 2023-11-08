def print2largest(arr, n):
	arr1=sorted(list(set(arr)))
	if len(arr1)>1:
		return arr1[-2]
	return -1
	
