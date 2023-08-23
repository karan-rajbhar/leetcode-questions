#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        wildCardPresent =  False

        if len(p) == 2 and '*' in p  and '.' in p:
            return True 
        if '*' in p or '.' in p:
            wildCardPresent = True

        if not wildCardPresent and s != p:
            return  False
        


            


        # if positionStar != -1 and positionDot == -1:
        #     tempPattern = p[0:positionStar]
        #     tempString = s[0:positionStar]
        #     if tempPattern ==  tempString:
        #         return True
            

# @lc code=end

