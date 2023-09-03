#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List
import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        digit_map={
            2:["a","b","c"],
            3:["d","e" , "f"],
            4:["g","h" ,"i"],
            5:["j" , "k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"]
        }
        alphabet_list = []
        for num in digits:
            alphabet_list.append(digit_map[int(num)])
        
        combinations = itertools.product(*alphabet_list)
        result_list=[]
        for combination in  combinations:
            result_list.append(''.join(combination))

        return result_list
    
solution = Solution()
print(solution.letterCombinations("23"))

        
        
# @lc code=end

