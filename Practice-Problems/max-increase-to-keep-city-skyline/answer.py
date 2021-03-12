class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_row = []
        max_col = []
        # Find the max in the row
        for row in grid:
            max_row.append(max(row))
        # Find the max in col 
        for i in range(len(grid[0])):
            max_i = float('-inf')
            for j in range(len(grid)):
                max_i = max(grid[j][i], max_i)
            max_col.append(max_i)
        # Find max totl sum of height added
        heights_added = 0
        for a in range(len(max_row)):
            for b in range(len(max_col)):
                height = min(max_row[a], max_col[b])
                heights_added += abs(grid[a][b] - height)
        return heights_added
