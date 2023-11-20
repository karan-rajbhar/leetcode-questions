#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
from typing import List
# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1={}
        
        for num in nums1:
            if dict1.get(num,False):
                dict1[num]=dict1[num]+1
            else:
                dict1[num]=1
        dict2={}
        
        for num in nums2:
            if dict2.get(num,False):
                dict2[num]=dict2[num]+1
            else:
                dict2[num]=1
        result=[]
        
        if len(dict1.keys())> len(dict2.keys()):
            for key in dict1.keys():
                if dict2.get(key,False):
                    if dict2[key] == dict1[key]:
                        for i in range(dict2[key]):
                            result.append(key)
                    else:
                        common_num = min(dict1[key],dict2[key])
                        for i in range(common_num):
                            result.append(key)
        else:
            for key in dict2.keys():
                if dict1.get(key,False):
                    if dict2[key] == dict1[key]:
                        for i in range(dict1[key]):
                            result.append(key)
                    else:
                        common_num = min(dict1[key],dict2[key])
                        for i in range(common_num):
                            result.append(key)

            
        return result
                
# @lc code=end

