# Swap case of each character in the string
def swap_case(s):
    data = []
    for i in s:
        if "a" <= i <= "z":
            data.append(chr(ord(i) - 32))
        elif "A" <= i <= "Z":
            data.append(chr(ord(i) + 32))
        else:
            data.append(i)
    return "".join(data)
