#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#

# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        for i in range(1, n):
            if self.sumall(i) == self.sumrem(i,n):
                return i
        return -1

    def sumall(self, n):
        return (n*(n+1))//2
    
    def sumrem(self,i,n):
        high = max(i,n)
        low = min(i,n)

        return (high*(high +1)//2 -(low-1)*(low)//2)        
        
# @lc code=end

