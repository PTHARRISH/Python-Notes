def diagonalDifference(arr):
    # Write your code here
    c=0
    d=0
    n=len(arr)
    for i in range(n):
        c+=arr[i][i]
        d+=arr[i][n-i-1]
        # a=c-d
    return abs(c-d)

n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)

print(result)

# For example, the square matrix arr is shown below:
# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = 1+5+9 = 15. 
# The right to left diagonal = 3+5+9=17. 
# Their absolute difference is |15-17| = 2.
