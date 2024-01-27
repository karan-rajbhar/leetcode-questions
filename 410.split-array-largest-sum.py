#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#
from typing import List
# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarray=0
            curSum =0
            
            for n in nums:
                curSum +=n
                if curSum > largest:
                    subarray +=1
                    curSum = n
            
            return subarray + 1 <= k
            
        left = max(nums)
        right = sum(nums)
        res = right


        while left <= right:
            mid =left+((right-left )//2)
            
            if canSplit(mid):
                res= mid
                right=mid-1
            else:
                left =mid+1

        return res
        
# @lc code=end

