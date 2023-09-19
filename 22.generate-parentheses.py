#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List
from itertools import combinations,product,permutations
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right , s):
           if len(s) == n* 2:
               result.append(s)
               return 
           if left < n:
               dfs(left +1 , right ,s +'(')
           if right < left:
               dfs(left ,  right +1 ,s +')')
               
        result = []

        dfs(0,0,'')
        return result


solution= Solution()
print(solution.generateParenthesis(6))
        
# @lc code=end

