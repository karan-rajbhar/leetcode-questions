#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            finalList = nums1 + nums2
            finalList = sorted(finalList)
            
            return self.findMiddle(finalList)

    def findMiddle(self, numList):
        if not numList :
                return "The List is empty"
        length = len(numList)
            
        if length % 2 != 0:
                middleIndex = length//2
                return numList[middleIndex]
        
        firstMiddleIndex = length //2-1
        secondMiddleIndex = length//2

        return (numList[firstMiddleIndex]+numList[secondMiddleIndex])/2                  
                   

        
# @lc code=end

