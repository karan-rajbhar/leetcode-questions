#
# @lc app=leetcode id=1980 lang=python3
#
# [1980] Find Unique Binary String
#
from typing import List
# @lc code=start
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        sorted_value = sorted([int(num,2) for num in nums])
        
        format_template = "0lengthb".replace('length',str(len(nums)))
        
        if 0 not in sorted_value:
            return format(0,format_template)

        prev=sorted_value[0]

        for i in range(1, len(sorted_value)):
            if prev+1 != sorted_value[i]:
                return format(prev+1, format_template)
            prev = sorted_value[i]
        
        return format(sorted_value[-1]+1, format_template)
        
# @lc code=end

