#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(board, word, index, row, col):
            # If the index reaches the end of the word, we found the word
            if index == len(word):
                return True
            
            # Check boundary conditions and if the cell matches the character
            if (row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or
                board[row][col] != word[index]):
                return False
            
            # Mark the cell as visited
            temp, board[row][col] = board[row][col], '#'
            
            # Explore neighboring cells recursively
            found = (dfs(board, word, index + 1, row + 1, col) or
                     dfs(board, word, index + 1, row - 1, col) or
                     dfs(board, word, index + 1, row, col + 1) or
                     dfs(board, word, index + 1, row, col - 1))
            
            # Reset the cell value to its original value
            board[row][col] = temp
            
            return found

        for i , row in enumerate(board):
            for j , column in enumerate(row):
                    # If the first character matches, start DFS
                if board[i][j] == word[0] and dfs(board, word, 0, i, j):
                    return True

        return False
        
# @lc code=end

