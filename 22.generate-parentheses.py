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
        brackets=("("*n)+(")"*n)
        print(brackets)
        result=set()
        for comb in permutations(brackets):
            joined_string="".join(comb)
            print(joined_string)
            if joined_string in result:
                continue

            if self.isValidParenthesis(joined_string):
                result.add(joined_string)
        
        return result

    def isValidParenthesis(self,str):
            stack=[]
            for char in str:
                if char in ["{","[","("]:
                    stack.append(char)
                else:
                    if not stack:
                        return False
                    
                    current_stack_bracket=stack.pop()
                    if char == "}":
                        if current_stack_bracket!='{':
                            return False
                    if char == "]":
                        if current_stack_bracket!='[':
                            return False
                    if char == ")":
                        if current_stack_bracket!='(':
                            return False
            if stack:
                return False
            return True       

solution= Solution()
print(solution.generateParenthesis(6))
        
# @lc code=end

