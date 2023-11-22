#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import List
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_freq={}
        for num in nums:
            if num in dict_freq:
                dict_freq[num]=dict_freq[num]+1
            else:
                dict_freq[num]=1
        
        
        sorted_dict=sorted(dict_freq,key=dict_freq.get)
        
        
        return sorted_dict[len(sorted_dict)-k:len(sorted_dict)]

        
# @lc code=end

