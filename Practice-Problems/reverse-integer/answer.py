class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        x_str = x_str[::-1]
        
        if x_str[-1] == '-':
            x_str = x_str[-1] + x_str[:-1]
            
        x_str = int(x_str)
        if x_str not in range(-2**31, 2**31):
            return 0
        return x_str
