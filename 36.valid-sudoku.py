#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
from typing import List


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check Row
        for row in board:
            rowDict = {}
            for num in row:
                if rowDict.get(num, None):
                    return False
                if num != ".":
                    rowDict[num] = True

        # Check Column
        for i in range(len(board)):
            columnDict = {}
            for j in range(len(board[i])):
                if columnDict.get(board[j][i], None):
                    return False
                if board[j][i] != ".":
                    columnDict[board[j][i]] = True
        
        # Check Square
        for i in range(0,len(board),+3):
            for j in range(0,len(board),+3):
                gridDict={}
                for row_index in range(i,i+3):
                    for column_index in range(j,j+3): 
                        if gridDict.get(board[row_index][column_index], None):
                            return False
                        if board[row_index][column_index] != ".":
                            gridDict[board[row_index][column_index]] = True
            



        return True


# solution = Solution()
# board = [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
# ]
# print(solution.isValidSudoku(board=board))
# @lc code=end
