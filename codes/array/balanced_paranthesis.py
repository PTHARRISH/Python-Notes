def paranthesis(s):
    while len(s)!=0:
        s=s.replace("()","")
        s=s.replace("[]","")
        s=s.replace("{}","")
        print(s)
    if len(s)==0:
        return True
    return False

s=input("enter the paranthesis: ")
print(paranthesis(s))