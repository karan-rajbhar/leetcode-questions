#
# @lc app=leetcode id=2321 lang=python3
#
# [2321] Maximum Score Of Spliced Array
#
from typing import List
# @lc code=start
class Solution:
    #using kaden's algorithm
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def go(nums1,nums2):
            best=0
            current=0

            for x , y in zip(nums1,nums2):
                current += x -y

                if current < 0:
                    current = 0
                best = max(best, current)
            
            return best
        best = 0
        best=max(best, sum(nums2)+go(nums1,nums2))
        best=max(best, sum(nums1)+go(nums2,nums1))

        return best 



    #Brute Force Approach
    def maximumsSplicedArrayBruteForce(self, nums1: List[int], nums2: List[int]) -> int:
        highest_sum=0
        length = len(nums1)
        
        for i in range(0, length):
            for j in range(0, length):
                #replace value of nums1 from index i to j with nums2 from index i to j in two temp_arrays
                temp_array1 = nums1.copy()
                temp_array1[i:j+1] = nums2[i:j+1]
                
                if sum(temp_array1) > highest_sum:
                    highest_sum = sum(temp_array1)

                temp_array2 = nums2.copy()
                temp_array2[i:j+1] = nums1[i:j+1]
                if sum(temp_array2) > highest_sum:
                    highest_sum = sum(temp_array2)
            
                
        return highest_sum
            

                
            


# @lc code=end

# solution = Solution()
# print(solution.maximumsSplicedArray([20,40,20,70,30], [50,20,50,40,20]))


