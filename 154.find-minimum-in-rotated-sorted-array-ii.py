#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
# @lc code=start
class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums)-1
                
        while left < right:
            mid = (left + right) // 2
            if nums[left] == nums[right]:
                left_pointer=left
                right_pointer=right
                
                while nums[left_pointer] == nums[right_pointer]:
                    if (left_pointer+1) <len(nums)-1:
                        left_pointer=left_pointer+1
                    else:
                        break
                left= left_pointer
                
            if nums[mid] > nums[right]:
                left = mid + 1

            else:
                right = mid
                
        if nums[left]<nums[right] or nums[left] == nums[right]:
            return nums[left]
        return nums[right]        
# @lc code=end

