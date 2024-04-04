#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        max_depth=0
        depth=0
        for char in s:
            if char == '(':
                stack.append(char)
                depth+=1
                max_depth = max(max_depth,depth)
            elif char == ')':
                stack.pop()
                depth -=1
                max_depth = max(max_depth,depth)

        return max_depth
                
# @lc code=end

