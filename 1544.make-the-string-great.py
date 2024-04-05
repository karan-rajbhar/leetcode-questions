#
# @lc app=leetcode id=1544 lang=python3
#
# [1544] Make The String Great
#

# @lc code=start
class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for char in s:
            if stack:
                if char.lower() == stack[-1].lower() and char != stack[-1]:
                    stack.pop()
                    continue
            stack.append(char)
            
        return "".join(stack) 
# @lc code=end

