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
        k = None
        j = None

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                k = i
                break
        # K is None this is the last permutation
        if k is None:
            nums.sort()
            return

        for i in range(len(nums) - 1, k, -1):
            if nums[i] > nums[k]:
                j = i
                break
        # swap

        temp = nums[k]
        nums[k] = nums[j]
        nums[j] = temp
        current_index = k + 1
        rest_sorted = sorted(nums[current_index:])
        nums[current_index:] = rest_sorted

    def nextPermutationBrutForce(self, nums: List[int]):
        sorted_nums = sorted(nums)
        combinations = list(dict.fromkeys(list(permutations(sorted_nums))))

        for index, permutation in enumerate(combinations):
            combo = list(permutation)
            if combo == nums:
                if index == len(combinations) - 1:
                    nums[:] = list(combinations[0])
                    break
                nums[:] = list(combinations[index + 1])
                break


# solution = Solution()
# nums=[5,4,7,5,3,2]
# solution.nextPermutation(nums)
# print(nums)

# @lc code=end


# (1, 2, 3, 4, 5),
# (1, 2, 3, 5, 4),
# (1, 2, 4, 3, 5),
# (1, 2, 4, 5, 3),
# (1, 2, 5, 3, 4),
# (1, 2, 5, 4, 3),
# (1, 3, 2, 4, 5),
# (1, 3, 2, 5, 4),
# (1, 3, 4, 2, 5),
# (1, 3, 4, 5, 2),
# (1, 3, 5, 2, 4),
# (1, 3, 5, 4, 2),
# (1, 4, 2, 3, 5),
# (1, 4, 2, 5, 3),
# (1, 4, 3, 2, 5),
# (1, 4, 3, 5, 2),
# (1, 4, 5, 2, 3),
# (1, 4, 5, 3, 2),
# (1, 5, 2, 3, 4),
# (1, 5, 2, 4, 3),
# (1, 5, 3, 2, 4),
# (1, 5, 3, 4, 2),
# (1, 5, 4, 2, 3),
# (1, 5, 4, 3, 2),
# (2, 1, 3, 4, 5),
# (2, 1, 3, 5, 4),
# (2, 1, 4, 3, 5),
# (2, 1, 4, 5, 3),
# (2, 1, 5, 3, 4),
# (2, 3, 1, 4, 5),
# (2, 3, 1, 5, 4),
# (2, 3, 4, 1, 5),
# (2, 3, 4, 5, 1),
# (2, 3, 5, 1, 4),
# (2, 3, 5, 4, 1),
# (2, 4, 1, 3, 5),
# (2, 4, 1, 5, 3),
# (2, 4, 3, 1, 5),
# (2, 4, 3, 5, 1),
# (2, 4, 5, 1, 3),
# (2, 4, 5, 3, 1),
# (2, 5, 1, 3, 4),
# (2, 5, 1, 4, 3),
# (2, 5, 3, 1, 4),
# (2, 5, 3, 4, 1),
# (2, 1, 5, 4, 3),
# (2, 5, 4, 1, 3),
# (2, 5, 4, 3, 1),
# (3, 1, 2, 4, 5),
# (3, 1, 2, 5, 4),
# (3, 1, 4, 2, 5),
# (3, 1, 4, 5, 2),
# (3, 1, 5, 2, 4),
# (3, 1, 5, 4, 2),
# (3, 2, 1, 4, 5),
# (3, 2, 1, 5, 4),
# (3, 2, 4, 1, 5),
# (3, 2, 4, 5, 1),
# (3, 2, 5, 1, 4),
# (3, 2, 5, 4, 1),
# (3, 4, 1, 2, 5),
# (3, 4, 1, 5, 2),
# (3, 4, 2, 1, 5),
# (3, 4, 2, 5, 1),
# (3, 4, 5, 1, 2),
# (3, 4, 5, 2, 1),
# (3, 5, 1, 2, 4),
# (3, 5, 1, 4, 2),
# (3, 5, 2, 1, 4),
# (3, 5, 2, 4, 1),
# (3, 5, 4, 1, 2),
# (3, 5, 4, 2, 1),
# (4, 1, 2, 3, 5),
# (4, 1, 2, 5, 3),
# (4, 1, 3, 2, 5),
# (4, 1, 3, 5, 2),
# (4, 1, 5, 2, 3),
# (4, 1, 5, 3, 2),
# (4, 2, 1, 3, 5),
# (4, 2, 1, 5, 3),
# (4, 2, 3, 1, 5),
# (4, 2, 3, 5, 1),
# (4, 2, 5, 1, 3),
# (4, 2, 5, 3, 1),
# (4, 3, 1, 2, 5),
# (4, 3, 1, 5, 2),
# (4, 3, 2, 1, 5),
# (4, 3, 2, 5, 1),
# (4, 3, 5, 1, 2),
# (4, 3, 5, 2, 1),
# (4, 5, 1, 2, 3),
# (4, 5, 1, 3, 2),
# (4, 5, 2, 1, 3),
# (4, 5, 2, 3, 1),
# (4, 5, 3, 1, 2),
# (4, 5, 3, 2, 1),
# (5, 1, 2, 3, 4),
# (5, 1, 2, 4, 3),
# (5, 1, 3, 2, 4),
# (5, 1, 3, 4, 2),
# (5, 1, 4, 2, 3),
# (5, 1, 4, 3, 2),
# (5, 2, 1, 3, 4),
# (5, 2, 1, 4, 3),
# (5, 2, 3, 1, 4),
# (5, 2, 3, 4, 1),
# (5, 2, 4, 1, 3),
# (5, 2, 4, 3, 1),
# (5, 3, 1, 2, 4),
# (5, 3, 1, 4, 2),
# (5, 3, 2, 1, 4),
# (5, 3, 2, 4, 1),
# (5, 3, 4, 1, 2),
# (5, 3, 4, 2, 1),
# (5, 4, 1, 2, 3),
# (5, 4, 1, 3, 2),
# (5, 4, 2, 1, 3),
# (5, 4, 2, 3, 1),
# (5, 4, 3, 1, 2),
# (5, 4, 3, 2, 1)
