#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left =0 
        right =n
        current=left +((right-left)//2)
        while left != right:
            mid = left +((right-left)//2)
            
            result = isBadVersion(mid)  # noqa: F821
            
            if result:
                right=mid
                current=mid
            else:
                left=mid+1
        
        if isBadVersion(left):  # noqa: F821
            return left
        return current
        
# @lc code=end

