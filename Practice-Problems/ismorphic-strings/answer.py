class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        if len(set(zip(s,t))) != len(set(s)):
            return False
        return True
                
