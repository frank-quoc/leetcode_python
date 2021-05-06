class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0
        
        while i < len(word1) or i < len(word2):
            letter1 = ""
            letter2 = ""
            
            if i < len(word1):
                letter1 = word1[i]
            if i < len(word2):
                letter2 = word2[i]
            i += 1
            result += letter1 + letter2
            
        return result
