#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        reverse =0
        isNegative = False
        if x < 0:
            x = x * -1
            isNegative = True
        while x > 0:
            lastDigit = x % 10
            reverse = (reverse * 10) + lastDigit
            x= int(x / 10)
        if isNegative:
            if reverse < -2147483648 or reverse > 2147483647:
                return 0
            return -abs(reverse)
        else:
            if reverse < -2147483648 or reverse > 2147483647:
                return 0
            return reverse
# @lc code=end

