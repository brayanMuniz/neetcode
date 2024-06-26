from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(used, wordLeft, x, y):
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or (x, y) in used:
                return False

            if board[x][y] != wordLeft[0]:
                return False

            if len(wordLeft) == 1:
                return True

            # Add the current position to the set of used positions
            used.add((x, y))
            # Recursively search in all 4 directions
            found = (dfs(used, wordLeft[1:], x - 1, y) or
                     dfs(used, wordLeft[1:], x + 1, y) or
                     dfs(used, wordLeft[1:], x, y - 1) or
                     dfs(used, wordLeft[1:], x, y + 1))
            # Backtrack by removing the current position from the set of used positions
            used.remove((x, y))

            return found

        for rowIdx in range(len(board)):
            for colIdx in range(len(board[0])):
                if board[rowIdx][colIdx] == word[0]:
                    if dfs(set(), word, rowIdx, colIdx):
                        return True

        return False

