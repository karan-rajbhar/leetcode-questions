#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#


# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for char in num:

            while stack and stack[-1] > char and k > 0:
                k -= 1
                stack.pop()

            stack.append(char)

        stack = stack[: len(stack) - k]
        return "".join(stack).lstrip('0') or "0"

# @lc code=end
