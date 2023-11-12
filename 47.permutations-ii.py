#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
from typing import List
import math

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        result = set()
        self.backtrack(nums,0,len(nums),result)
        return list(result)

    def backtrack(self, nums , current , length , result):
        if current == length:
            result.add(tuple(nums[:]))
            return
        
        for i in range(current,length):
            nums[current] , nums[i] = nums[i] , nums[current]
            self.backtrack(nums,current+1,length,result)
            nums[current] , nums[i] = nums[i] , nums[current]


# solution = Solution()
# print(solution.permuteUnique([1,1,2]))

# @lc code=end

