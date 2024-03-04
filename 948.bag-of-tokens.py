#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#

# @lc code=start
from typing import List
from collections import  deque 
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        tokens = deque(tokens)
        score = 0
        max_score = 0
        while tokens and (tokens[0] <= power or score > 0):
            if tokens[0] <= power:
                power -= tokens.popleft()
                score += 1
                max_score = max(max_score, score)
            else:
                power += tokens.pop()
                score -= 1
                
        return max_score
            


                

        
# @lc code=end

