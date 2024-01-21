# 345. Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

# while and if condition:
def reverseVowels(s):
        left,right=0,len(s)-1
        Vowels=set("aeiouAEIOU")
        result=list(s)
        while left<right:
            if result[left] not in Vowels:
                left += 1
            if result[right] not in Vowels:
                right -= 1
            if result[right] in Vowels and result[left] in Vowels:
                result[left],result[right] = result[right],result[left]
                right -= 1
                left += 1
            
        return ''.join(result)

# while loop only
def reverseVowels(s):
    i,j=0,len(s)-1
    vowels=set("aeiouAEIOU")
    result=list(s)
    while i<j:
        while i<j and result[i] not in vowels:
            i+=1
        while i<j and result[j] not in vowels:
            j-=1
        result[i],result[j]=result[j],result[i]
        i+=1
        j-=1
    return "".join(result)

print(reverseVowels("hello"))

# if else condition
def reverseVowels(s):
        i=0
        j=len(s)-1
        list1=["a","e","i","o","u","A","E","I","O","U"]
        s=list(s)
        while i<j:
            if s[i] in list1 and s[j] in list1:
                s[i],s[j]= s[j],s[i]
                i+=1
                j-=1
            elif s[i] not in list1 and s[j] in list1:
                i+=1
            elif s[i] in list1 and s[j] not in list1:
                j-=1
            else:
                i+=1
                j-=1
    
        return "".join(s)

print(reverseVowels("hello world"))