#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
from typing import List
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # for i in set(nums):
        #     if nums.count(i)> len(nums)//2:
        #         return i
        
        #Moore Voting Algorithm

        count=0
        candidate=0

        for num in nums:
            if count ==0:
                candidate = num
            if num == candidate:
                count +=1
            else:
                count -=1

        return candidate        
# @lc code=end

