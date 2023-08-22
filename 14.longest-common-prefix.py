#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            strs.sort(key=str.lower)
            shortest= strs[0]
            longest = strs[-1]
            longestPrefix=""
            for i in range(0,len(shortest)):
                if shortest[i] == longest [i]:
                    longestPrefix=longestPrefix+shortest[i]
                else:
                    break
                                        
                
            return longestPrefix
        
# @lc code=end

