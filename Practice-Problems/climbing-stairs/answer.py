class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        steps_lst = [0] * n
        steps_lst[0] = 1
        steps_lst[1] = 2
        
        for i in range(2, len(steps_lst)):
            steps_lst[i] = steps_lst[i-1] + steps_lst[i-2]
        
        return steps_lst[-1]
