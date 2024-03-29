class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_element = max(nums)
        result=0
        max_count = 0
        left=0
        for i in range(len(nums)):
            if nums[i]== max_element:
                max_count+=1

            while max_count==k:
                if nums[left] == max_element:
                    max_count-=1
                
                left+=1
            
            result+=left

        return result
