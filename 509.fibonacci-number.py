#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
cache = {}
class Solution:
    
    def fib(self, n: int) -> int:
        if n in cache:
            return cache[n]
        
        if n < 2:
            return n
        
        else:
            result = self.fib(n-1)+ self.fib(n-2)
        
        cache[n] = result
        
        return result        
# @lc code=end

