#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        self.ans = []                                  
        def traverse(candid, arr,sm):
            if sm == target: self.ans.append(arr)                    
            if sm >= target: return                    
            for i in range(len(candid)):               
                traverse(candid[i+1:], arr + [candid[i]], sm+candid[i])   
        traverse(candidates,[], 0)
        sorted_ans=[sorted(item) for item in self.ans]

        ans=[]
        [ans.append(item) for item in sorted_ans if item not in ans]
        return ans
    
# solution = Solution()
# print(solution.combinationSum2([10,1,2,7,6,1,5],8))

# @lc code=end

