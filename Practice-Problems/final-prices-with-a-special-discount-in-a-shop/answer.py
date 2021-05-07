class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for j in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[j]:
                i = stack.pop()
                prices[i] -= prices[j]
            stack.append(j)
        return prices
        
