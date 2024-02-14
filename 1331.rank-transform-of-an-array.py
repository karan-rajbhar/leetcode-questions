#
# @lc app=leetcode id=1331 lang=python3
#
# [1331] Rank Transform of an Array
#
from typing import List
# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        rank = {}
        rank_val = 1
        for val in sorted_arr:
            if val not in rank:
                rank[val] = rank_val
                rank_val += 1
        return [rank[val] for val in arr]


        
# @lc code=end

