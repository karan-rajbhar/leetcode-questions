#
# @lc app=leetcode id=1991 lang=python3
#
# [1991] Find the Middle Index in Array
#
from typing import List
# @lc code=start
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)

        for i, num in enumerate(nums):
            right -= num
            if left == right:
                return i
            left += num
        
        return -1
        
# @lc code=end

