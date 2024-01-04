def subarray(arr,s):
    n=len(arr)
    sum1=0
    b=0
    e=-1
    for i in range(n):
        sum1=sum1+arr[i]
     #   print(sum1)
        while(sum1>s):
            sum1=sum1-arr[b]
            b=b+1
        if(sum1 == s):
            e=i
            break
    if (sum1!=s or b>e):
         return [-1]
    return [b+1,e+1]

arr=[int(i) for i in input("Enter the array: ").split(",")]
s=int(input("Target: "))
print(subarray(arr,s))