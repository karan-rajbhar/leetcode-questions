#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalindromeSubString = ""
        if len(s) == 1 or self.checkIfPalindrome(s) :
            return s

        for firstIndex in range(0, len(s)+1):
            for secondIndex in range(0, len(s)+1):
                currentString = s[firstIndex:secondIndex]
                if (
                    self.checkIfPalindrome(currentString)
                    and len(currentString) > len(longestPalindromeSubString)
                    
                ):
                    longestPalindromeSubString = currentString

        return longestPalindromeSubString

    def checkIfPalindrome(self, string: str):
        if string == string[::-1]:
            return True
        return False
    

# @lc code=end
