#
# @lc app=leetcode id=1208 lang=python3
#
# [1208] Get Equal Substrings Within Budget
#

# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        
        left = 0
        right = 0
        maxLength = 0
        currentSum = 0
        
        while right < len(costs):
            currentSum += costs[right]
            
            while currentSum > maxCost:
                currentSum -= costs[left]
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
            right += 1
        
        return maxLength        
# @lc code=end

