#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#
from typing import List
# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if trust == []:
            if n==1:
                return 1
            else:
                return -1

        trusting_people=set()
        trusted_by={}
        for i in trust:
            trusting_people.add(i[0])
            if i[1] in trusted_by:
                trusted_by[i[1]].add(i[0])
            else:
                trusted_by[i[1]]=set()
                trusted_by[i[1]].add(i[0])

        for key, value in trusted_by.items():
            if len(value) == n-1 and key not in trusting_people :
                return key

        return -1        
# @lc code=end

