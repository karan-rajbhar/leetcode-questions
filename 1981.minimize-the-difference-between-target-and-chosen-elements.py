#
# @lc app=leetcode id=1981 lang=python3
#
# [1981] Minimize the Difference Between Target and Chosen Elements
#
from typing import List
# @lc code=start
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:

        # 1. Find the minimum and maximum possible sum of the elements in the matrix
        # 2. Create a set of all possible sums of the elements in the matrix
        # 3. Find the closest sum to the target
        # 4. Return the difference between the closest sum and the target

        # 1. Find the minimum and maximum possible sum of the elements in the matrix
        min_sum = sum(min(row) for row in mat)
        max_sum = sum(max(row) for row in mat)

        # 2. Create a set of all possible sums of the elements in the matrix
        possible_sums = {0}
        for row in mat:
            possible_sums = {x + y for x in possible_sums for y in row}

        # 3. Find the closest sum to the target
        closest_sum = min(possible_sums, key=lambda x: abs(x - target))

        # 4. Return the difference between the closest sum and the target
        return abs(closest_sum - target)
        
# @lc code=end

