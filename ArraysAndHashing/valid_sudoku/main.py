# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:

#     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     Only the filled cells need to be validated according to the mentioned rules.
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate rows
        for row in board:
            if not self.is_unit_valid(row):
                print("Row check failed:", row)
                return False
        
        # Validate columns
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.is_unit_valid(column):
                print("Column check failed:", column)
                return False
        
        # Validate 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(box):
                    print("Box check failed at:", i, j, box)
                    return False
        
        return True
    
    def is_unit_valid(self, unit: List[str]) -> bool:
        unit = [i for i in unit if i != '.']
        return len(unit) == len(set(unit))
            
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
x = Solution()
print(x.isValidSudoku(board=board))