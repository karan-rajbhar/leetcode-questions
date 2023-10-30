#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        points=self.find_gaps(height)
        result=0

        for point in points:
            result +=self.calculate_rain(point.first_point,point.second_point,point.diff)
        
        return result
    def find_gaps(self,height:List[int]):
        pass

    def calculate_rain(self,first_point, second_point, diff):
        pass        
# @lc code=end

