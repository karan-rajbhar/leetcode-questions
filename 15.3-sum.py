#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List
from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        result =set()
        negative , positive ,zero = [] ,[] ,[]
        
        for num in nums:

            if num > 0:
                positive.append(num)
            elif num < 0:
                negative.append(num)
            else:
                zero.append(num)

        negativeSet , positiveSet = set(negative) , set(positive)

        if zero :
            for num in positive:
                if -1*num in negative:
                    result.add((-1*num,0,num))
            if len(zero) >=3:
                result.add((0,0,0))

        for x, y in combinations(negative, 2):
            target = -1 * (x + y)
            if target in positiveSet:
                result.add(tuple(sorted([x, y, target])))

        for x, y in combinations(positive, 2):
            target = -1 * (x + y)
            if target in negativeSet:
                result.add(tuple(sorted([x, y, target])))
        return result 

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))
# @lc code=end
