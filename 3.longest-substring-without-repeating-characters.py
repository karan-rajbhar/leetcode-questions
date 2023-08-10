#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        maxLength = 0
        left =0
        charSet= set()

        for right in range(length):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength , right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left = left + 1
                charSet.add(s[right])

        return maxLength


# @lc code=end