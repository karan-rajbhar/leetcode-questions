#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points.sort(key=lambda x: (x[0], x[1]))
        result = []

        for i in points:
            if result:
                intersection = self.find_intersection(result[-1] , i)
                if intersection:
                    result.pop()
                    result.append(intersection)
                else:
                    result.append(i)
            else:
                result.append(i)
        
        return len(result)        
    def find_intersection(self,range1, range2):
        # Sort the ranges
        range1 = sorted(range1)
        range2 = sorted(range2)

        # Check for intersection
        if range1[1] >= range2[0] and range2[1] >= range1[0]:
            return (max(range1[0], range2[0]), min(range1[1], range2[1]))
        else:
            return None
        
# @lc code=end

