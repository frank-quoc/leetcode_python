class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x = len(needle)
        for i in range(len(haystack) - x + 1):
            if haystack[i:i+x] == needle:
                return i
        return -1
    
        # better solution
        # return haystack.find(needle)
