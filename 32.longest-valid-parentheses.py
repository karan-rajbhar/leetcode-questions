#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#


# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 2 and not self.isValid(s):
            return 0

        if self.isValid(s):
            return len(s)

        left = s[1:]
        right = s[:-1]

        if self.isValid(left):
            return len(left)

        if self.isValid(right):
            return len(right)

        if self.longestValidParentheses(right):
            return self.longestValidParentheses(right)

        if self.longestValidParentheses(left):
            return self.longestValidParentheses(left)

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if not stack:
                    return False

                current_stack_bracket = stack.pop()
                if char == ")":
                    if current_stack_bracket != "(":
                        return False
        if stack:
            return False
        return True


# solution = Solution()
# print(solution.longestValidParentheses(s=")()())"))
# @lc code=end
