#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
from typing import List
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        result = []

        for i in range(len(matrix)):
            result.append([])
            for j in range(len(matrix[i])):
                result[i].insert(0,matrix[j][i])

        matrix[:] = result
        
solution = Solution()
solution.rotate([[1,2,3],[4,5,6],[7,8,9]])
# @lc code=end

