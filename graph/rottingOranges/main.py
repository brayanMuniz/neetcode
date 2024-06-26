from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        allOranges = set()
        markedOranges = set()
        updatedOranges = []
        
        # Initialize the sets and lists
        for rowIdx, row in enumerate(grid):
            for colIdx, col in enumerate(row):
                if col == 2:
                    updatedOranges.append((rowIdx, colIdx))
                    markedOranges.add((rowIdx, colIdx))
                if col == 1 or col == 2:
                    allOranges.add((rowIdx, colIdx))
        
        # If there are no initially rotting oranges but there are fresh oranges, return -1
        if len(updatedOranges) == 0 and len(allOranges) > len(markedOranges):
            return -1

        minutes = 0

        while len(updatedOranges) > 0:
            newOranges = []
            for row, col in updatedOranges:
                # Spread to adjacent cells if they are fresh
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    newRow, newCol = row + dr, col + dc
                    if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        newOranges.append((newRow, newCol))
                        markedOranges.add((newRow, newCol))
            
            updatedOranges = newOranges
            if len(newOranges) > 0:
                minutes += 1

        # After processing, check if all fresh oranges have been marked
        return minutes if allOranges == markedOranges else -1
