class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prevStr = self.countAndSay(n-1)
        
        i = 1
        count = 1
        num = prevStr[0]
        ans = ''
        
        while i < len(prevStr):
            if prevStr[i] == num:
                count += 1
                i += 1
            else:
                ans += str(count) + num
                count = 0
                num = prevStr[i]
        ans += str(count) + num
        
        return ans
