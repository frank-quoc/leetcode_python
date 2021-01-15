class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True
        if num == 0:
            return False
        
        i = 0
        ugly = [5, 3, 2]
        while i < len(ugly):
            if num % ugly[i] == 0:
                num /= ugly[i]
                continue
            else:
                i += 1
        if num == 1:
            return True
        return False
