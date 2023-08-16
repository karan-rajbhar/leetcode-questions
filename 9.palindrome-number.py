#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        if x < 0:
            return False
        reverse = 0
        while x > 0:
            lastDigit =  x%10
            x=int(x/10)
            reverse=(reverse*10)+lastDigit
        if reverse == original:
            return True
        return False
        
# @lc code=end

