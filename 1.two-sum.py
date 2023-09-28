#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

from typing import List


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        position_dict = {}

        for index, num in enumerate(nums):
            remaining = target - num
            
            #Check if needed number exist in position_dict if exist return return answer
            if position_dict.get(remaining, None) is not None:
                return [position_dict.get(remaining), index]
            
            position_dict[num] = index
        return []




# @lc code=end
