#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#
from typing import List
# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        temp_dict={}
        
        for num1 in nums1:
            for num2 in nums2:
                temp_dict[num1+num2]=temp_dict.setdefault(num1+num2,0)+1
        
        result=0
        for num3 in nums3:
            for num4 in nums4:
                if -(num3+num4) in temp_dict:
                    result+=temp_dict[-(num3+num4)]
                    
        
        return result
                    
            
            
                
# @lc code=end

