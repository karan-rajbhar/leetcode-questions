#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

from typing import List


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        result = []
        first = 0
        last = len(nums) - 1
        self.findTarget(first, last, nums, target, result)
        if result:
            return [result[0], result[-1]]

        return [-1, -1]

    def findTarget(self, i, j, num_list, target, result):
        if num_list[i] == target:
            result.append(i)

        if i == j:
            return -1

        mid = int((i + j) / 2)
        self.findTarget(i, mid, num_list, target, result)
        self.findTarget(mid + 1, j, num_list, target, result)


# solution = Solution()
# print(solution.searchRange([],8))
# @lc code=end
