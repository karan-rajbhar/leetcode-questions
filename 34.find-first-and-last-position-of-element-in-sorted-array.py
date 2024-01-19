#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

from typing import List


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums)==0:
            return [-1,-1]
        
        if len(nums) == 1:
            if nums[0]==target:
                return [0,0]
            return [-1,-1]
            
        
        left , right = 0, len(nums)-1
        
        while left +1 < right:
            mid =(left+right)//2
            
            if nums[mid] == target:
                first=mid
                last=mid
                while (first-1)>=0:
                    if nums[first-1]==target:
                        first=first-1
                    else:
                        break
                while last+1<=len(nums)-1:
                    if nums[last+1] == target:
                        last = last+1
                    else:
                        break
                return [first,last]
            elif nums[mid]<target:
                left=mid
            else:
                right= mid
         
        if nums[left] == target:
            first=left
            last=left
            while (first-1)>=0:
                if nums[first-1]==target:
                    first=first-1
                else:
                    break
            while last+1<=len(nums)-1:
                if nums[last+1] == target:
                    last = last+1
                else:
                    break
            return [first,last]
            
        
        if nums[right] == target:
            first=right
            last=right
            while (first-1)>=0:
                if nums[first-1]==target:
                    first=first-1
                else:
                    break
            while last+1<=len(nums)-1:
                if nums[last+1] == target:
                    last = last+1
                else:
                    break
            return [first,last]
        
        return [-1,-1]


# solution = Solution()
# print(solution.searchRange([],8))
# @lc code=end
