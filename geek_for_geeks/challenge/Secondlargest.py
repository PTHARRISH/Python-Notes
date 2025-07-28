def getSecondLargest(arr):
    n = len(arr)
    first = second = float("-inf")
    if n < 2:
        return -1
    else:
        for i in arr:
            if i > first:
                second = first
                first = i
            elif i > second and i != first:
                second = i
        if second == float("-inf"):
            return -1
        return second

