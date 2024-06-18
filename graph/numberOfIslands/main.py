from typing_extensions import List

# When you find an island, find all other part of the island recursively, remove them from the array. 
# keep going until you get to the end of the list. 
class Solution:
    def removeIsland(self,grid: List[List[str]], x, y):
        if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) -1 or grid[x][y] == '0':
            return
        
        grid[x][y] = '0'

        self.removeIsland(grid, x + 1, y)
        self.removeIsland(grid, x - 1, y)
        self.removeIsland(grid, x, y + 1)
        self.removeIsland(grid, x, y - 1)


    def numIslands(self, grid: List[List[str]]) -> int:
        totalAmount = 0
        for rowIdx, row in enumerate(grid):
            for colIdx, col in enumerate(row):
                if col == '1':
                    totalAmount += 1
                    self.removeIsland(grid, rowIdx, colIdx)
                    
        return totalAmount

