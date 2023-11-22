# reversal_algorithm_for_array_rotation
# Function to reverse arr[]
def reverseArray(arr,d):
	c=(arr[d:])+(arr[:d])
	return c
# Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
d=2
print(reverseArray(arr,d))
