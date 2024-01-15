class Solution:
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
    
    