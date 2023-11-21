#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_dict= dict([(char,True) for char in jewels])
        count=len([i for i in stones if jewel_dict.get(i,False)])
        
        return count
        
# @lc code=end

