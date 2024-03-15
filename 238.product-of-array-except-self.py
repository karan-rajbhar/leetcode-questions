#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)
        prefix =1 

        for i in range(len(nums)):
            result[i] = prefix

            prefix *= nums[i]

        postfix=1

        for i in range(len(nums)-1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

        
# @lc code=end

