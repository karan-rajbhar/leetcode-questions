#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    # o(nlogn)
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     square= [i*i for i in nums]

    #     return sorted(square)
    # o(n)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        index=len(nums)-1
        result=[0]*len(nums)
        while left <= right:
            left_square= nums[left]*nums[left]
            right_square =nums[right]*nums[right]

            if left_square <= right_square:
                result[index] = right_square
                right-=1

            else:

                result[index] = left_square
                left+=1

            index -=1

        return result
        
# @lc code=end

