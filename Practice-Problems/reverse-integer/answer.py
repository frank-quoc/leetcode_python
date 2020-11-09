class Solution:
    def reverse(self, x: int) -> int:
        x_rev = str(x)
        x_rev = x_str[::-1]
        
        if x_rev[-1] == '-':
            x_rev = x_rev[-1] + x_rev[:-1]
            
        x_rev = int(x_revstr)
        if x_rev not in range(-2**31, 2**31):
            return 0
        return x_rev
