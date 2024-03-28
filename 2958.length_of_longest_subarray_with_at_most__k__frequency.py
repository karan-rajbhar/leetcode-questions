from collections import defaultdict
class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter_dict=defaultdict(int)
        max_count=0
        start=0

        for end in range(len(nums)):
            counter_dict[nums[end]]+=1
            while counter_dict[nums[end]] > k:
                counter_dict[nums[start]]-=1
                start+=1
            max_count=max(max_count,end-start+1)
            
        return max_count