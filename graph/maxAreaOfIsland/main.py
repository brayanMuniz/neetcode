from typing import List

# Traverse each, if a 1 add up to its val, mark it, find the total amount and return 
class Solution:
    def dfs(self, grid: List[List[int]], x: int, y: int, total: int) -> int:
        if x < 0 or y < 0 or x > len(grid) - 1  or y > len(grid[0]) - 1 or grid[x][y] == 0:
            return 0

        total = 1
        grid[x][y] = 0

        total += self.dfs(grid, x + 1, y, total)
        total += self.dfs(grid, x - 1, y, total)
        total += self.dfs(grid, x , y + 1, total)
        total += self.dfs(grid, x , y -1, total)

        return total

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for rowIdx, row in enumerate(grid):
            for colIdx, col in enumerate(row):
                if col == 1:
                        maxArea = max(maxArea, self.dfs(grid, rowIdx, colIdx, 0))
        return maxArea


        
