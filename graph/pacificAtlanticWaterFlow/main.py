from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(x, y, visited, prev_height):
            if ((x, y) in visited or
                x < 0 or x >= rows or
                y < 0 or y >= cols or
                heights[x][y] < prev_height):
                return

            visited.add((x, y))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                dfs(x + dx, y + dy, visited, heights[x][y])

        # Run DFS from Pacific Ocean borders
        for i in range(rows):
            dfs(i, 0, pacific_reachable, heights[i][0]) # Left Border
            dfs(i, cols - 1, atlantic_reachable, heights[i][cols - 1]) # Right Border

        for j in range(cols):
            dfs(0, j, pacific_reachable, heights[0][j]) # Top Border
            dfs(rows - 1, j, atlantic_reachable, heights[rows - 1][j]) # Bottom border

        # Intersection of both reachable sets gives the result
        res = list(pacific_reachable & atlantic_reachable)
        return res
        
