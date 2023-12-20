#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0:
            return True
        if len(s)==1:
            return False
        stack=[]
        for i in s:
            if i in ["(","[","{"]:
                stack.append(i)
            else:
                if not stack:
                    return False
                
                if i == ")":
                    if stack.pop() != "(":
                        return False
                if i == "}":
                    if stack.pop() != "{":
                        return False
                if i == "]":
                    if stack.pop() != "[":
                        return False
        if stack:
            return False
        
        return True
        

solution= Solution()
print(solution.isValid("(]"))
        
# @lc code=end

