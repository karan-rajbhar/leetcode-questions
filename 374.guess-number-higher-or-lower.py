#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left=1
        right=n
        while left <= right:
            middle = left + ((right-left)//2)
            if guess(middle) == 0:  # noqa: F821
                return middle
            if guess(middle) == -1: # noqa: F821
                right = middle -1
            if guess(middle) == 1: # noqa: F821
                left = middle +1

        
# @lc code=end

