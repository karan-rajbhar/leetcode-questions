#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
from itertools import permutations
from typing import List
# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
    def nextPermutationBrutForce(self,nums: List[int]) :
        sorted_nums= sorted(nums)
        
        combinations =  list(permutations(sorted_nums))
        for index ,permutation in enumerate(combinations):
            combo= list(permutation)
            if combo == nums:
                if index == len(combinations)-1:
                    return combinations[0]
                return combinations[index+1]
        

solution = Solution()
print(solution.nextPermutationBrutForce([3,2,1]))
        
# @lc code=end

