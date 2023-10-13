#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

from typing import List


# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first_index = 0
        last_index = len(nums) - 1
        mid=0
        while first_index < last_index :
            
            mid = int((first_index +last_index) / 2)
            if nums[mid] < target:
                first_index = mid + 1
            elif nums[mid] > target:
                last_index = mid
            else:
                return mid

        if target > nums[-1]:
            return last_index+1
        else:
            return last_index


# solution = Solution()
# print(solution.searchInsert([1, 3, 5, 6], 7))
# @lc code=end
