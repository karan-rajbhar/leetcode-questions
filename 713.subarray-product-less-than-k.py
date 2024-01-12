#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#
from typing import List
# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        length = len(nums)
        if set(nums) == {1}:
            if k == 1:
                return 0
            if k == 0:
                return 0
            else:
                return length * (length + 1) // 2
        
        for i in range(length):
            product = 1
            curr_index = i
            while curr_index < length:
                product *= nums[curr_index]
                if product < k:
                    count += 1
                    
                if product >= k:
                    break
                curr_index += 1
            
        return count


    # Brute force solution
    def numSubarrayProductLessThanKBruteForceSolution(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                product = 1
                
                for num in nums[i:j+1]:
                    product *= num
                if product < k:
                    count += 1
        
        return count

# @lc code=end

# solution = Solution()
# print(solution.numSubarrayProductLessThanK([10,5,2,6], 100))
