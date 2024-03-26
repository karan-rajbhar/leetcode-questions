#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
from typing import List
# @lc code=start
class Solution:
    
    # #Time complexity: O(nlogn) Space complexity: O(1)
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     smallest_int=1
    #     nums.sort()
    #     for num in nums:
    #         if num == smallest_int:
    #             smallest_int +=1
        
    #     return smallest_int
    
    #Time complexity: O(n) Space complexity: O(1)

    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        def swap(i,j):
            nums[i] , nums[j] = nums[j] , nums[i]

        n = len(nums)
        for i in range(n):
            while 1<= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(i, nums[i]-1)

        
        for i in range(n):
            if i+1 != nums[i]:
                return i+1
        
        return n+1

# @lc code=end

# solution= Solution()
# print(solution.firstMissingPositive([2,1,0]))
