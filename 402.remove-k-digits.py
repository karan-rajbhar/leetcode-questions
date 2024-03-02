#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for char in num:
            while k > 0 and stack and stack[-1] > char:
                k -=1
                stack.pop()
            
            stack.append(char)
        
        stack = stack[:len(stack)-k]
        result =[]
        last_leading_zero=True
        for char in stack:
            if char == '0' and last_leading_zero:
                continue
            
            last_leading_zero=False
            result.append(char)
        if result==[]:
            return "0"
        return "".join(result)
        
# @lc code=end

