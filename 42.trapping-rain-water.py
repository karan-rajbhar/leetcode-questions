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
        print(points)
        for point in points:
            result +=self.calculate_rain(point.first_index,point.second_index)
        
        return result
    def find_gaps(self,height:List[int]):
        points=[]
        first_index=None
        second_index=None
        for index in range(len(height)):
            if first_index is not None and second_index is not None :
                if height[index] < height[second_index] :
                    points.append((first_index,second_index))
                    first_index=second_index
                    second_index=None
                    continue
            if height[index] != 0 and first_index is None:
                first_index=index
                continue

            if first_index is not None:
                if height[index] > height[first_index]:
                    second_index=index

        return points

    def calculate_rain(self,first_index, second_index ):
        pass  

solution = Solution()
solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])

# @lc code=end

