#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dict={}
        
        for index in range(len(s)):
            if dict.get(s[index]):
                dict[s[index]]=dict[s[index]]+1
            else:
                dict[s[index]]=1
    
            
        for key in dict.keys():
            if dict[key]==1:
                return s.rfind(key)
        
        return -1
                
# @lc code=end

