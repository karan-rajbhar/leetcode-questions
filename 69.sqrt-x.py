#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left =0
        right=x
        result=0
        
        while left <= right:
            
            middle = left + ((right-left)//2)
            if middle**2 ==x :
                return middle
            
            if middle**2 >x:
                right = middle -1
                
            if middle**2<x:
                left = middle+1
                result= middle
        
        return result        
# @lc code=end

