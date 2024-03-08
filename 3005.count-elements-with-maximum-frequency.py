
#
# @lc app=leetcode id=997 lang=python3
#
# [3005] Count Elements With Maximum Frequency
#
# @lc code=start
from collections import Counter


class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)

        m = max(freq.values())

        return sum( v for v in freq.values() if v ==m)
# @lc code=end
