# Insertion Sort:
# Insertion sort is a very simple method to sort numbers in an ascending or descending order. 
# This method follows the incremental method. 
# It can be compared with the technique how cards are sorted at the time of playing a game.
# This is an in-place comparison-based sorting algorithm. 
# Here, a sub-list is maintained which is always sorted. 
# For example, the lower part of an array is maintained to be sorted. 
# An element which is to be 'inserted' in this sorted sub-list, has to find its appropriate place 
# and then it has to be inserted there. Hence the name, insertion sort.


# Pseudocode
# Algorithm: Insertion-Sort(A)
# for j = 2 to A.length
#    key = A[j]
#    i = j – 1
#    while i > 0 and A[i] > key
#       A[i + 1] = A[i]
#       i = i -1
#    A[i + 1] = key


# code:
def insertionSort(arr):
	n = len(arr) # Get the length of the array
	
	if n <= 1:
		return # If the array has 0 or 1 element, it is already sorted, so return

	for i in range(1, n): # Iterate over the array starting from the second element
		key = arr[i] # Store the current element as the key to be inserted in the right position
		j = i-1
		while j >= 0 and key < arr[j]: # Move elements greater than key one position ahead
			arr[j+1] = arr[j] # Shift elements to the right
			j -= 1
		arr[j+1] = key # Insert the key in the correct position

# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)

