#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#
from typing import List
# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff_index={0:-1}
        res=0
        count=0

        for i, num in enumerate(nums):
            count += 1 if num==1 else -1

            if count in diff_index:
                res=max(res, i-diff_index[count])
            else:
                diff_index[count]=i

        return res

        
# @lc code=end

