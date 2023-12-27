#
# @lc app=leetcode id=2259 lang=python3
#
# [2259] Remove Digit From Number to Maximize Result
#

# @lc code=start
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        for i in range(len(number)-1):
            if number[i] == digit:
                if number[i+1] > number[i]:
                    return number[:i] + number[i+1:]
        
        return number[:number.rindex(digit)]+number[number.rindex(digit)+1:]
# @lc code=end

