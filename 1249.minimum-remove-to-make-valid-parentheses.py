#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count=0
        result=[]
        for char in s:
            if char == '(':
                count+=1
                result.append(char)
            elif char == ')' and count>0:
                result.append(char)
                count-=1
            elif char != ')':
                result.append(char)
        

        filtered = []
        for char in result[::-1]:
            if char == '(' and count > 0:
                count-=1
            else:
                filtered.append(char)
        
        return "".join(filtered[::-1])
        
# @lc code=end

