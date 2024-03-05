#
# @lc app=leetcode id=1750 lang=python3
#
# [1750] Minimum Length of String After Deleting Similar Ends
#

# @lc code=start
class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        right=len(s)-1
        while left<right and right <= len(s)-1:
            
            if s[right] == s[left]:
                right-1
                left+1
                while right >=0 and s[right-1] ==s[left] and right != left:
                    right-=1
                
                while left <= len(s)-1 and left != right and s[right] == s[left+1]:
                    left+=1
            else:
                break
            
            right-=1
            left+=1

        return len(s[left:right+1])
        
# @lc code=end

