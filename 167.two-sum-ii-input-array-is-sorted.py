#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        set_numbers=set(numbers)

        for i in range(len(numbers)):
            find = target - numbers[i]
            if find in set_numbers:
                result_index=self.binary_search(numbers,i, len(numbers),find)
                
                if result_index != -1:
                    return [i+1,result_index+1]
            
            
    def binary_search(self, nums,left,right,target):
        left=left
        right=right
        
        while left < right:
            mid = left+((right-left))//2
            
            if nums[mid]== target:
                return mid
            
            if nums[mid]> target:
                right=mid 
                
            if nums[mid]< target:
                left=mid+1
        return -1        
# @lc code=end

