#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

from typing import List

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2=0

        while True:
            slow= nums[slow]
            slow2 =nums[slow2]

            if slow == slow2:
                return slow        
# @lc code=end

