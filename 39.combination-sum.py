#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []                                  
        def traverse(candid, arr,sm):
            if sm == target: self.ans.append(arr)                    
            if sm >= target: return                    
            for i in range(len(candid)):               
                traverse(candid[i:], arr + [candid[i]], sm+candid[i])   
        traverse(candidates,[], 0)

        return self.ans
    
solution = Solution()
solution.combinationSum([2,3,6,7],7)
