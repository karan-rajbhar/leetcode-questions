#
# @lc app=leetcode id=1984 lang=python3
#
# [1984] Minimum Difference Between Highest and Lowest of K Scores
#
from typing import List
# @lc code=start
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 0

        nums.sort()
        
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))                
# @lc code=end

