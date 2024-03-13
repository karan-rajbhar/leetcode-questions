#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import List
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = int("".join([str(i) for i in digits]))
        number +=1
        string=str(number)

        return [ int(i) for i in string]
        
# @lc code=end

