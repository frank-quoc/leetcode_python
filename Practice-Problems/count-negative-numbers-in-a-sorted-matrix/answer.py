class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = 0
        nums = len(grid[0])
        for row in grid:
            lower = 0
            upper = nums - 1
            while lower < upper:
                mid = (lower + upper) // 2
                if row[mid] < 0:
                    upper = mid
                else:
                    lower = mid + 1
            neg += nums - (lower if row[lower] < 0 else nums)
        return neg
    
