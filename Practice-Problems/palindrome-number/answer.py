class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Using strings
        return str(x) == str(x)[::-1]
        
        # without changing number to string
        if x < 0:
            return False
        if (x % 10 == 0) and (x != 0):
            return False
        
        # Checks to see if the reversed is = to the orginal
        reversed = 0
        while x > reversed:
            reversed = reversed * 10 +  x % 10
            x = x // 10
        
        if x == reversed: # for cases like 11
            return True
        elif x == reversed // 10: # for ever other number
            return True
        else:
            return False
