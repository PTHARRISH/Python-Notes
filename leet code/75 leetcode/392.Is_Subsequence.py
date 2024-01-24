# 392. Is Subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting 
# some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false


def isSubsequence(s, t):
    i = 0
    j = 0
        # Loop until one of the pointers reaches the end
    while i < len(s) and j < len(t):
            # If the characters match, move both pointers forward
        if s[i] == t[j]:
            i += 1
            j += 1
                # If the characters don't match, move only the pointer of t forward
        else:
            j += 1
        # Return true if the pointer of s reaches the end of s, false otherwise
    return i == len(s)

s ="abc"
t ="ahbgdc"
print(isSubsequence(s,t))