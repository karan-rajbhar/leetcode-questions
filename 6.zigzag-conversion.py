#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s)==1:
            return s
        
        string=['']* numRows
        index=0
        step=1
        for char in s:
            string[index] = string[index]+char
            if index ==0:
                step =1
            elif index == numRows-1:
                step=-1
            index = index +step
        
        return ''.join(string)
            
                     
            
# @lc code=end

