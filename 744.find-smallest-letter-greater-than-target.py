#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#
from typing import List
# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)
        
        while left < right:
            mid = left+((right-left))//2
            
            if letters[mid] == target:
                for i in range(mid+1,len(letters)):
                    if letters[i] != target:
                        return letters[i]
                else:
                    return letters[0]            
            if letters[mid] < target:
                left = mid+1
            
            if letters[mid] > target:
                right = mid
                
        if left == 0:
            return letters[0]
        
        if right==len(letters):
            return letters[0]
        

        return letters[left]
        
# @lc code=end

