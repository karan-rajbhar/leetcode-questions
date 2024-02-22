#
# @lc app=leetcode id=1981 lang=python3
#
# [1981] Minimize the Difference Between Target and Chosen Elements
#
from typing import List
# @lc code=start
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # 1. Create a set of all possible sums of the elements in the matrix
        possible_sums = {0}
        for row in mat:
            possible_sums = {x + y for x in possible_sums for y in row}

        # 2. Find the closest sum to the target
        closest_sum = min(possible_sums, key=lambda x: abs(x - target))

        # 3. Return the difference between the closest sum and the target
        return abs(closest_sum - target)
        
# @lc code=end

