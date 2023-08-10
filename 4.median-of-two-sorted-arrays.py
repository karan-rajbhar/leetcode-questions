#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            final_list = nums1 + nums2
            final_list = sorted(final_list)
            
            return self.find_middle(final_list)

    def find_middle(self, num_list):
        if not num_list :
                return "The List is empty"
        length = len(num_list)
            
        if length % 2 != 0:
                middle_index = length//2
                return num_list[middle_index]
        
        first_middle_index = length //2-1
        second_middle_index = length//2

        return (num_list[first_middle_index]+num_list[second_middle_index])/2                  
                   

        
# @lc code=end

