#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from typing import List
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize a result list with the same length as temperatures, filled with 0s
        result = [0] * len(temperatures)
        stack=[]

        for i ,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex= stack.pop()
                result[stackIndex] = i - stackIndex
            
            stack.append([temp,i])
        
        return result


# solution = Solution()
# print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))
        
# @lc code=end

