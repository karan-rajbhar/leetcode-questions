#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#


# @lc code=start
from math import sqrt


class Solution:
    # recursive solution
    def pivotIntegerRecursive(self, n: int) -> int:
        if n == 1:
            return 1

        def recursive(n, i):

            if i > n:
                return -1

            if ((i * (i + 1)) // 2) == (n * (n + 1) // 2 - (i - 1) * (i) // 2):
                return i
            return recursive(n, i + 1)

        return recursive(n, 1)
    #iterative solution
    def pivotIntegerIterative(self, n: int) -> int:
        if n == 1:
            return 1
        for i in range(1, n):
            if ((i * (i + 1)) // 2) == (n * (n + 1) // 2 - (i - 1) * (i) // 2):
                return i
        return -1
    
    #mathematical solution
    def pivotInteger(self, n: int) -> int:
        temp = (n * n + n) // 2
        sq = int(sqrt(temp))
        if sq * sq == temp:
            return sq
        return -1

    #     if n==1:
    #         return 1
    #     for i in range(1, n):
    #         if self.sumall(i) == self.sumrem(i,n):
    #             return i
    #     return -1

    # def current_sum(self, n):
    #     return (n*(n+1))//2

    # def sumrem(self,i,n):
    #     high = max(i,n)
    #     low = min(i,n)

    #     return (high*(high +1)//2 -(low-1)*(low)//2)


# solution = Solution()
# print(solution.pivotInteger(8))
# @lc code=end
