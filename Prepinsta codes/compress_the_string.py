# compress the string using hash map

def compress_string(s):
    result=""
    hashmap={}
    for c in s:
        if c in hashmap:
            hashmap[c]+=1 # IF character already in hashmap increment its value
        else:
            hashmap[c]=1 # else it will create hashmap and assign a value is 1
    for key,value in hashmap.items():
        result+=key # add each key in a string (abcd are the keys)
        if value>1:
            result+=str(value)
    return result
    
    
n=input("enter the string: ")
print(compress_string(n))
