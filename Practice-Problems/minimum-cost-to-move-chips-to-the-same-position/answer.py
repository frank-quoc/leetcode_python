class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd_start = 0 
        even_start = 0
        for i in range(len(position)):
            if position[i] % 2 == 0:
                odd_start += 1
            else:
                even_start += 1
        return min(odd_start, even_start)
