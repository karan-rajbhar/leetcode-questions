#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first=0
        last=len(nums)-1
        return self.findTarget(first,last,nums, target)

    def findTarget(self, i ,j, num_list,target):
        if num_list[i] == target:
            return i
                
        if i==j:
            return -1

        mid= int((i+j)/2)

        return max(self.findTarget(i,mid, num_list , target),self.findTarget(mid+1,j,num_list, target))        

# solution = Solution()
# print(solution.search([4,5,6,7,0,1,2],0))
# @lc code=end

