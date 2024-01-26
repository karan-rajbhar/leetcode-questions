#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#

from typing import List
# @lc code=start
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        left =0
        right = nums[-1] - nums[0]
        
        while left < right:
            mid = (left+right)//2
            
            if self.is_kth_smallest_pair(nums, k , mid):
                right = mid
            else:
                left =mid +1
        
        return left
    
    def is_kth_smallest_pair(self,nums, k ,mid):
        left = 0
        count=0
        for right in range(1, len(nums)):
            while (nums[right] - nums[left]) > mid:
                left +=1
            
            count+=right-left
        
        if count >= k:
            return True
        
        return False
                
        
                
# @lc code=end

