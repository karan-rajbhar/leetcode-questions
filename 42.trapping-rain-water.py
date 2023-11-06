#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
            left, right = 0, len(height) - 1
            leftMax = rightMax = trappedWater = 0

            while left <= right:
                leftMax = max(leftMax, height[left])
                rightMax = max(rightMax, height[right])

                if leftMax <= rightMax:
                    trappedWater += max(0, leftMax - height[left])
                    left += 1
                else:
                    trappedWater += max(0, rightMax - height[right])
                    right -= 1

            return trappedWater

# solution = Solution()
# print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

# @lc code=end

