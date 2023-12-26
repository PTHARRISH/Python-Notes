# check input is integer or not
try:
    num=int(input("enter the number:"))
    # a=float(num)
except ValueError as e:
    print("given input is not a number",e)


def num():
    num1=input("enter the number: ")
    a=num1.isnumeric()
    if a:
        return True
    else:
        return False
    
print(num())