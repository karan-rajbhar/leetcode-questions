#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import List
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        result = []
        self.backtrack(nums, [], result)
        return result

    def backtrack(self, nums, current, result):
        if len(current) == len(nums):
            result.append(current[:])
            return

        for num in nums:
            if num in current:
                continue
            current.append(num)
            self.backtrack(nums, current, result)
            current.pop()
        
# solution = Solution()
# print(solution.permute([1,2,3]))
# @lc code=end

