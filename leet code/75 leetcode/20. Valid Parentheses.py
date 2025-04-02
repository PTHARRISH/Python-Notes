# 20. Valid Parentheses
def valid_parathesis(s):
    stacks = list()
    data = {'(':')','{':'}','[':']'}
    for i in s:
        if i not in data:
            stacks.append(i)
        else:
            if not stacks:
                return False
            elif data[stacks[-1]]==i:
                stacks.pop()
            else:
                return False
    if not stacks:
        return False
    return True
                
    
    
str_data = input('enter the data: ')
print(valid_parathesis(str_data))