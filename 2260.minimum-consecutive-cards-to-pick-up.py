#
# @lc app=leetcode id=2260 lang=python3
#
# [2260] Minimum Consecutive Cards to Pick Up
#

# @lc code=start
from typing import List
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        card_map={}
        for  i in range(len(cards)):
            if cards[i] in card_map:
                card_map[cards[i]].append(i)
            else:
                card_map[cards[i]]=[i]
        minimum=-1
        # print(card_map)
        for card in card_map:
            if len(card_map[card])>1:
                curr_list = card_map[card]
                curr_list.sort()
                # Iterate over the sorted list
                for i in range(len(curr_list) - 1):  # Subtract 1 to avoid IndexError
                    # Calculate the difference between the current element and the next one
                    diff = curr_list[i+1] - curr_list[i]
                    # If this difference is less than the current minimum or if minimum is -1, update the minimum
                    if minimum == -1 or diff < minimum:
                        minimum = diff
                    
        if minimum !=-1:
            return minimum+1 
        return minimum     
# solution = Solution()
# solution.minimumCardPickup([3,4,2,3,4,7])
# solution.minimumCardPickup([95,11,8,65,5,86,30,27,30,73,15,91,30,7,37,26,55,76,60,43,36,85,47,96,6])   
# @lc code=end

