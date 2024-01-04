def missing(arr,n):
    total=(n*(n+1))//2
    sum_of_a=sum(arr)
    return total-sum_of_a

s=int(input("n: ")) # n=4
arr=[int(i) for i in input("Enter the array: ").split(",")] # [1,2,4]
if len(arr)<=s:
    print(missing(arr,s)) # 3
        