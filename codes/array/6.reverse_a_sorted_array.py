def printOrder(arr, n):
    arr.sort() 
    mid = n//2 
    s1 = arr[:mid] 
    s2 = arr[:mid:-1] 
    print(s1+s2) # Driver code
arr = [ 5, 4, 6, 2, 1, 3, 8, -1 ]
n = len(arr)
printOrder(arr, n)

