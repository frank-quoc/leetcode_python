VOWELS = "aeiouAEIOU"

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = 0
        mid = len(s) // 2
        for i in range(mid):
            if s[i] in VOWELS: count += 1
            if s[mid+i] in VOWELS: count -=1
        return count == 0
