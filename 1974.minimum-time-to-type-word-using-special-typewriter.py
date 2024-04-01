#
# @lc app=leetcode id=1974 lang=python3
#
# [1974] Minimum Time to Type Word Using Special Typewriter
#

# @lc code=start
class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        result=0
        last_char = "a"
        for char in word:
            if last_char == char:
                result+=1
            else:
                result+=self.minimumDistance(last_char , char)+1
            last_char = char

        return result

    def minimumDistance(self,start,end):
        clockwise_distance = abs((ord(start)-97) - (ord(end)-97))
        
            # Calculate counterclockwise distance
        counterclockwise_distance = 26 - clockwise_distance
        return min(clockwise_distance , counterclockwise_distance)
        
                
# @lc code=end

