#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
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
print(solution.isValid("(]"))
        
# @lc code=end

