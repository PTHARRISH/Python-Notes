# Given an unsorted array arr[] of size N. 
# Rotate the array to the left (counter-clockwise direction) by D steps, where D is a positive integer. 
def rotated_array(arr,D,N):
    D=D%N #2%5=2 and if 10%5=0 then it will add in D value
    # print(N)
    # print(D)
    arr[:]=arr[D:]+arr[:D]
    return arr

arr=[int(x) for x in input("enter the array numbers: ").split(',') ]
n=len(arr)
d=int(input('enter the number: '))
print(rotated_array(arr,d,n))