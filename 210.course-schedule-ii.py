#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
from typing import List
from collections import deque, defaultdict
# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if prerequisites==[]:
            return [i for i in range(numCourses)]
        graph = defaultdict(list)
        in_degree = [0]*numCourses
        for Course,Pre in prerequisites:
            graph[Pre].append(Course)
            in_degree[Course]+=1
        
        queue = deque()
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)
        res = []

        while queue:
            cur = queue.popleft()
            res.append(cur)
            for next in graph[cur]:
                in_degree[next]-=1
                if in_degree[next]==0:
                    queue.append(next)
        
        if len(res)==numCourses:
            return res
        
        return []

        

        
                
# @lc code=end

