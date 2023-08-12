#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        num_next = numRows-2
        array=[]
        count=0
        column=[]
        for index in(0, len(s)+1) :
            
            if count != numRows:
                column.append(s[index])
                count= count+1

            if count== numRows:
                array.append(column)
                column = []
                count = 0

            
            
            
            

# @lc code=end

