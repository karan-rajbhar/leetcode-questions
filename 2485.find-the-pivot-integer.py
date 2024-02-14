#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#


# @lc code=start
class Solution:

    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1

        def recursive(n, i):

            if i > n:
                return -1

            if ((i * (i + 1)) // 2) == (n * (n + 1) // 2 - (i - 1) * (i) // 2):
                return i
            return recursive(n, i + 1)

        return recursive(n, 1)



# solution = Solution()
# print(solution.pivotInteger(8))
# @lc code=end
