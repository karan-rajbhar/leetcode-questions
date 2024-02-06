#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
from typing import List
# @lc code=start

class Solution:
    #DP solution
    def getRowDPS(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row


    #recusrive solution
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        
        current_row = [1]

        previous_row = self.getRow(rowIndex-1)

        for i in range(1,len(previous_row)):
            current_row.append(previous_row[i-1]+previous_row[i])

        current_row.append(1)

        return current_row
        
# @lc code=end

