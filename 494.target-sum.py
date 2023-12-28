#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from typing import List
# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache={} # (index,total)-> # of ways
        
        def backtrack(index, total):
            if len(nums) == index:
                return 1 if target== total else 0
            if (index,total) in cache:
                return cache[index,total]
            cache[(index,total)]=(backtrack(index+1,total+nums[index])+backtrack(index+1,total-nums[index]))    
            return cache[(index,total)]
            
        
        
        return backtrack(0,0)        
# @lc code=end

