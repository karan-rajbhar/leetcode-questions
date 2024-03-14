#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#
from collections import defaultdict
from typing import List

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        n= len(nums)
        memo=defaultdict(int)
        count=0
        prefix_sum=0
        memo[0]=1
        for i in range(n):
            prefix_sum+=nums[i]

            remove = prefix_sum-goal

            count +=memo[remove]

            memo[prefix_sum] +=1

        return count
       



# @lc code=end

