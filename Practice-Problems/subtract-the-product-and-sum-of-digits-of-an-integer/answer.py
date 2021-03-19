class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_dig = 0 
        prod = 1
        while n > 9:
            dig = n % 10
            n = n // 10
            sum_dig += dig
            prod *= dig
        return prod*n - sum_dig - n 
