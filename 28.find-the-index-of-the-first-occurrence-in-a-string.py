#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:


    def strStr(self, haystack: str, needle: str) -> int:
        hash_needle=hash(needle)
        for i in range(len(haystack)-len(needle)+1):
            if hash(haystack[i:i+len(needle)]) == hash_needle:
                return i
        
        return -1

    #Online solution joke solution
    def strStr1(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        
# solution =Solution()
# print(solution.strStr("hello","ll"))
# @lc code=end

