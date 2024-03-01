#
# @lc app=leetcode id=2864 lang=python3
#
# [2864] Maximum Odd Binary Number
#

# @lc code=start
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = s.count('1')
        array=["0"]*len(s)
                
        for i in range(0,count-1):
            array[i]="1"
        
        array[-1]="1"
        

        return "".join(array)
        
# @lc code=end

