#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        
        if str1[:len(str2)] == str2:
            if len(str1) == len(str2):
                return str2
            return self.gcdOfStrings(str1[len(str2):], str2)
        else:
            return ""
        
        
# @lc code=end

