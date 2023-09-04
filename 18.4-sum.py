#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
from typing import List
import itertools
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums=sorted(nums)
        results=set()
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                left = j+1
                right =  n-1

                while left < right:
                    total = nums[i] + nums[left] + nums[right] +nums[j]
                    if total > target:
                        right -=1
                    elif total < target:
                        left+=1
                    else:
                        results.add(tuple(sorted((nums[i], nums[left], nums[right],nums[j]))))
                        left+=1
                        right-=1

        return results




# @lc code=end

