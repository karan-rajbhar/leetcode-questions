#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict={}
        
        for index in range(len(s)):
            if dict.get(s[index],None):
                if dict[s[index]] != t[index]:
                    return False
            if t[index] in dict.values():
                if s[index] not in dict.keys():
                    return False
            dict[s[index]]=t[index]
        
        return True        
# @lc code=end

