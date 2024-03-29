#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num ==1:
            return True
        left = 0
        right=num
        
        while left < right:
            mid = left+((right-left)//2)
            
            if mid * mid ==num:
                return True
            
            if mid * mid > num:
                right = mid
            if mid * mid < num:
                left= mid+1
        return False
# @lc code=end

