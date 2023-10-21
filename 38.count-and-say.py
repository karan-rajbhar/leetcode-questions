#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        string = '1'
        
        for _ in range(n - 1):
            string = self.make_count(string)

        return string

    @staticmethod
    def make_count(n: str) -> str:
        return ''.join(f'{sum(1 for _ in gr)}{key}' for key, gr in groupby(n))        
# @lc code=end

