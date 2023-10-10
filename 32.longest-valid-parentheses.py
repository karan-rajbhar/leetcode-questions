#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#


# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_length = 0
        start = -1

        for i in range(len(s)):
            print(start)
            if s[i] == '(':
                stack.append(i)
            else:
                if not stack:
                    start = i
                else:
                    stack.pop()
                    if not stack:
                        max_length = max(max_length, i - start)
                    else:
                        max_length = max(max_length, i - stack[-1])

        return max_length

solution = Solution()
print(solution.longestValidParentheses(s=")()())"))
# @lc code=end
