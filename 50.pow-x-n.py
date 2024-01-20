#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def recursive(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            result = recursive(x,n // 2)
            result= result* result
            
            if n%2 == 0:
                return result
            else:
                return x*result
        
        result = recursive(x,abs(n))
        
        if n<0:
            return 1/result
        else:
            return result
        

# solution = Solution()
# print(solution.myPow(2.00000, 10))
        
# @lc code=end

