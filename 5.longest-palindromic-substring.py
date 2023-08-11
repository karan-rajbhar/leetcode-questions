#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalindromeSubString = ""
        if len(s) == 1:
            longestPalindromeSubString = s
        if self.checkIfPalindrome(s):
            return s

        for first_index in range(0, len(s)+1):
            for second_index in range(0, len(s)+1):
                current_string = s[first_index:second_index]
                if (
                    self.checkIfPalindrome(current_string)
                    and len(current_string) > len(longestPalindromeSubString)
                    
                ):
                    longestPalindromeSubString = current_string

        return longestPalindromeSubString

    def checkIfPalindrome(self, string: str):
        if string == string[::-1]:
            return True
        return False
    

# @lc code=end
