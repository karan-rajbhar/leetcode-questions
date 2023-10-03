#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
from itertools import permutations
from typing import List
# @lc code=start
class Solution:
    def nextPermutationBrutForce(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
    def nextPermutation(self,nums: List[int]) :
        sorted_nums= sorted(nums)
        combinations =  list(dict.fromkeys(list(permutations(sorted_nums))))        
        
        for index ,permutation in enumerate(combinations):
            combo= list(permutation)
            if combo == nums:
                if index == len(combinations)-1:
                    nums[:] = list(combinations[0])
                    break
                nums[:] = list(combinations[index+1])
                break


# solution = Solution()
# nums=[1,5,1]
# solution.nextPermutation(nums)
# print(nums)        
# @lc code=end

