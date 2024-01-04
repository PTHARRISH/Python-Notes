def isPowerofTwo(n):
    if n == 0:
        return False
    return (n&(n-1))==0  
# 256&255==0 because it convert the value in binary and (&) opertaor 
# get common value there is no common value is found then the output 0==0  

n=int(input("Enter the number: ")) # 256
print(isPowerofTwo(n)) # True