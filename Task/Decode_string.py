def decode_string(s):
    stack = []
    curr_num = 0
    curr_str = ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = 0
            # Handle numbers with more than one digit
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            curr_num = num
        elif s[i] == "{" or s[i] == "(":
            # Push current status into stack and reset
            stack.append((curr_str, curr_num))
            curr_str = ""
            curr_num = 0
            i += 1
        elif s[i] == "}" or s[i] == ")":
            # Pop from stack and decode
            last_str, num = stack.pop()
            curr_str = last_str + curr_str * num
            i += 1
        else:
            curr_str += s[i]
            i += 1
    return curr_str


specialString = input()
print(decode_string(specialString))
