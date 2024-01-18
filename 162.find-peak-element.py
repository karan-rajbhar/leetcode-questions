#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
from typing import List
# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
                
        def recursive(left,right,nums):
            if left == right:
                return 0
            
            mid = left+((right-left)//2)
            
            if (mid-1)>=0 and (mid+1)<=len(nums)-1: 
                if nums[mid-1]< nums[mid] and nums[mid+1] < nums[mid]:
                    return mid
                
            elif (mid+1) == len(nums):
                if nums[mid-1]<nums[mid]:
                    return mid
            
            elif (mid-1) == -1:
                if nums[mid+1]<nums[mid]:
                    return mid
                
            return max(recursive(left,mid,nums),recursive(mid+1,right,nums))
        return recursive(0,len(nums),nums)
    
# @lc code=end
        
        

