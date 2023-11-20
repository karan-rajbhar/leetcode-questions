#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
from typing import List
# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_map={}
        for index in range(len(nums)):
            if dict_map.get(nums[index]) is not None:
                if abs(dict_map[nums[index]]-index) <= k:
                    return True
                else:
                    dict_map[nums[index]]= index
            else:
                dict_map[nums[index]]=index
                

        return False
                    
# @lc code=end

