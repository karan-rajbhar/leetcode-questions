#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
from typing import List
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest_int=1
        nums.sort()
        for num in nums:
            if num == smallest_int:
                smallest_int +=1
        
        return smallest_int
        
# @lc code=end

# solution= Solution()
# print(solution.firstMissingPositive([2,1,0]))
