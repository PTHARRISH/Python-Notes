# Minimum and Maximum in the sum array
def miniMaxSum(arr):
    # Write your code here
    news1=0
    news2=0
    arr.sort()
    for i in range(len(arr)-1):
        news1+=arr[i]
    for j in range(1,len(arr)):
        news2+=arr[j]
    print(news1,news2)
        
a=list(map(int,input().split())) # 1 2 3 4 5 6 7
miniMaxSum(a) 
# output: 21 27
