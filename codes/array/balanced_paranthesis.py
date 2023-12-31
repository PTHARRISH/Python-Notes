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


def is_balanced(expression):
    stack = []
    opening_symbols = '({['
    closing_symbols = ')}]'

    for char in expression:
        if char in opening_symbols:
            stack.append(char)
        elif char in closing_symbols:
            if not stack:
                return False  # No matching opening symbol
            last_opening = stack.pop()
            if opening_symbols.index(last_opening) != closing_symbols.index(char):
                return False  # Mismatched opening and closing symbols

    return not stack  # If stack is empty, all symbols are balanced

# Example usage:
expression1 = "({[()]})"
expression2 = "{[({[)})"

print("Expression 1 is balanced:", is_balanced(expression1))
print("Expression 2 is balanced:", is_balanced(expression2))