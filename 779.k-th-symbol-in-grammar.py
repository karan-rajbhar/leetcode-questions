#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        curr = 0
        left = 0
        right = 2**(n-1)

        for _ in range(n-1):
            mid = (left + right) // 2
            if k <= mid:
                right = mid
            else:
                left = mid+1
                curr= 0 if curr else 1
        
        return curr
# @lc code=end

