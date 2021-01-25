class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        curr_max = max(candies)
        boolean_big = []
        for candy in candies:
            if candy + extraCandies >= curr_max:
                boolean_big.append(True)
            else:
                boolean_big.append(False)
        return boolean_big
