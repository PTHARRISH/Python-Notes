# Generator

def generateFibonacciNumbers(n: int) -> List[int]: 
    # Write your code here
    a=0
    b=1
    d=1
    while d<=n:
        yield a
        c = a + b
        a = b
        b = c
        d+=1