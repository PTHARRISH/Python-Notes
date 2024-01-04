def missing(arr,n):
    total=(n*(n+1))//2
    sum_of_a=sum(arr)
    return total-sum_of_a

s=int(input("n: "))
arr=[int(i) for i in input("Enter the array: ").split(",")]
if len(arr)<=s:
    print(missing(arr,s))
        