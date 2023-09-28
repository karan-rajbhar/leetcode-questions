#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
from typing import List
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    
        for i in range(0,len(nums)):
            if nums[i] == val:
                for j in range(i+1,len(nums)):
                    if nums[j] != val:
                        temp=nums[i]
                        nums[i] = nums[j]
                        nums[j]=temp
        count=0
        for num in nums:
            if num == val:
                break
            count +=1


        return count
        

# solution = Solution()
# nums=[0,1,2,2,3,0,4,2]
# val=2
# print(solution.removeElement(nums, val))

# print(nums)
# @lc code=end

