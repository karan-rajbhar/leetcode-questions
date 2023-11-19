#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#
from typing import List
# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict={}
        
        for index in range(len(list1)):
            if dict.get(list1[index],False):
                dict[list1[index]].append(index)
            else:
                dict[list1[index]]=[index]
        
        for index in range(len(list2)):
            if dict.get(list2[index],False):
                dict[list2[index]].append(index)
            else:
                dict[list2[index]]=[index]
            
                
        
        result_dict={}    
        for key in dict.keys():
            if len(dict[key]) >1:
                result=sum(dict[key])
                if result_dict.get(result,False):
                    result_dict[result].append(key)
                else:
                    result_dict[result]=[key]
        first=min(result_dict.keys())
        
        return result_dict[first]
            
            
            
                
# @lc code=end

