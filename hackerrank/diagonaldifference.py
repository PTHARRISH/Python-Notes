
def diagonalDifference(arr):
    # Write your code here
    c=0
    d=0
    n=len(arr)
    for i in range(n):
        c+=arr[i][i]
        d+=arr[i][n-i-1]
    return abs(c-d)

n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)

print(result)