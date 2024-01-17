#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right= len(nums)-1

        while left <= right:
            mid = left + (right - left)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right=mid-1
                else:
                    left= mid+1
            else:
                if nums[mid] <= target <= nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1

# solution = Solution()
# print(solution.search([4,5,6,7,0,1,2],0))
# @lc code=end

