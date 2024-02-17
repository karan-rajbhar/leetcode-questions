#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = [0, 0, 0, 0, 0]
        for c in text:
            if c == 'b':
                count[0] += 1
            elif c == 'a':
                count[1] += 1
            elif c == 'l':
                count[2] += 1
            elif c == 'o':
                count[3] += 1
            elif c == 'n':
                count[4] += 1
        count[2] = count[2] // 2
        count[3] = count[3] // 2
        return min(count)
        
# @lc code=end

