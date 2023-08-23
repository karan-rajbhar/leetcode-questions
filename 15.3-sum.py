#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            threeSumList = []
            numberOfTriplets = len(nums)//3
            indexPositionDict={}
            for i in range(1, numberOfTriplets+1):
                triplets = []
                index = 0
                loopBreak=True
                
                while loopBreak:
                    print(len(triplets))
                    if len(triplets) == 3 and sum(triplets) == 0:
                        loopBreak=False
                    if triplets == []:
                        triplets.append(nums[index])
                        index+=1
                        
                    if len(triplets) == 2:
                        remaining = 0 - sum(triplets)
                        if nums[index] == remaining:
                            triplets.append(nums[index])
                    
                    if len(triplets) == 1:
                        triplets.append(nums[index])

                    index+=1
                    
                        
                threeSumList.append(triplets)
                
            return threeSumList        
# @lc code=end

