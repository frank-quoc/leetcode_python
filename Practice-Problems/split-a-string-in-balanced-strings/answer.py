class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal_strs = 0
        count = 0
        for letter in s:
            if letter == "R":
                count += 1
            else: 
                count -= 1
            if count == 0:
                bal_strs += 1
        return bal_strs
