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
    
    
    def mergeAlternate(self, word1: str, word2: str) -> str:
        answer=""
        min_length=min(len(word1),len(word2))
        for i in range(min_length):
            answer+=word1[i]+word2[i]
        
        answer+=word1[min_length:]
        answer+=word2[min_length:]
        return answer


    