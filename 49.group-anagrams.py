#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from typing import List
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {}

        for s in strs:
            temp="".join(sorted(s))
            
            if temp in result:
                result[temp].append(s)
            else:
                result[temp] = [s]

        return list(result.values())


solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) 
# @lc code=end

