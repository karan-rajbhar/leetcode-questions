#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#
from typing import List
# @lc code=start
class Solution:
    #solution using two stacks
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative_stack=[]
        positive_stack=[]

        for i in nums:
            if i < 0:
                negative_stack.append(i)
            else:
                positive_stack.append(i)
        
        result =[]
        for i in range(len(positive_stack)):
            result.append(positive_stack[i])
            result.append(negative_stack[i])


        return result        
# @lc code=end

