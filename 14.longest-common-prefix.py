#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            shortest,longest=self.sortList(strs)
            tempLongestPrefix=""
            longestPrefix=""
            for i in range(0,len(shortest)):
                if shortest[i] == longest [i]:
                    tempLongestPrefix=tempLongestPrefix+shortest[i]
                else:
                    break
                
            for word in strs:
                if tempLongestPrefix in word[0:len(tempLongestPrefix)]:
                    continue
                else:
                    for i in range(0,len(tempLongestPrefix)):
                        if tempLongestPrefix[i]==word[i]:
                            longestPrefix=longestPrefix+tempLongestPrefix[i]
                        else:
                            return longestPrefix
                                
                        
                
            return tempLongestPrefix
    def sortList(self,lst):
        lst.sort(key=len)
        return lst[0],lst[-1]
        
# @lc code=end

