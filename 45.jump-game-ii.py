#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
from typing import List


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0

        jumps = 0
        current_max_reach = 0
        next_max_reach = 0

        for i in range(len(nums) - 1):
            next_max_reach = max(next_max_reach, i + nums[i])

            if i == current_max_reach:
                jumps += 1
                current_max_reach = next_max_reach

        return jumps


# @lc code=end
