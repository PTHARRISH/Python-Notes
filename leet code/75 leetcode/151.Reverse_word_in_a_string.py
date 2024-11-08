# 151. Reverse Words in a String

# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. 
# The returned string should only have a single space separating the words. 
# Do not include any extra spaces.

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

def reverse_words(s):
    l=s.split()[::-1]
    return " ".join(l)
s="a good   example"
print(reverse_words(s))

# example good a

# 2nd method using while loop
def reverse_words(s):
    result=""
    s=s.strip()
    i=0
    word=s.split()
    n=len(word)-1
    while i<=n:
        result+=word[n]+' '
        n-=1
    return result[:-1]

s="  hello world  "
print(reverse_words(s))

# world hello