#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
from typing import List
# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
            
        def helperFunc(index, s):
            if index == len(s)//2:
                return
            temp_char = s[index]
            s[index] = s[-(index+1)]
            s[-(index+1)] = temp_char
            
            helperFunc(index+1,s)
        
        helperFunc(0,s)
        
# @lc code=end

