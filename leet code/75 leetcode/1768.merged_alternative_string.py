# 1768. Merge Strings Alternately

# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.
 
# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r


class Solution:
    # using for zip method
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=[]
        for i,j in zip(word1,word2):
            merged.append(i)
            merged.append(j)
        if len(word1)>len(word2):
            merged.append(word1[len(word2):])
        elif len(word2)>len(word1):
            merged.append(word2[len(word1):])
        return "".join(merged)
    
    # using for loop
    def mergeAlternate(self, word1: str, word2: str) -> str:
        answer=""
        min_length=min(len(word1),len(word2))
        for i in range(min_length):
            answer+=word1[i]+word2[i]
        
        answer+=word1[min_length:]
        answer+=word2[min_length:]
        return answer
    
    # using while loop
    def mergeAlternate1(self, word1: str, word2: str) -> str:
        answer=""
        i=0
        min_length=min(len(word1),len(word2))
        while i<min_length:
            answer+=word1[i]+word2[i]
            i+=1
        answer+=word1[min_length:]
        answer+=word2[min_length:]
        return answer

    