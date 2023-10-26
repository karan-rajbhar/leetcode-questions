#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans = []                                 
        def traverse(candid, arr,sm):
            if sm == target :
                self.ans.append(arr)                    
            if sm >= target: return                    
            for i in range(len(candid)):
                if i==0 or candid[i] != candid[i-1]:               
                    traverse(candid[i+1:], arr + [candid[i]], sm+candid[i])   
        traverse(candidates,[], 0)

        return self.ans
    
# solution = Solution()
# print(solution.combinationSum2([10,1,2,7,6,1,5],8))

# @lc code=end

