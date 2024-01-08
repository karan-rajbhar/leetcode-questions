#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
from typing import List
# @lc code=start
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if prerequisites==[]:
            return [i for i in range(numCourses)]
        graph={}
        courses=set()        
        for preq in prerequisites:
            if preq[1] in graph:
                graph[preq[1]].append(preq[0])
            else:
                graph[preq[1]]=[preq[0]]
            courses.add(preq[0])
            courses.add(preq[1])
        
        for course in courses:
            path=[]
            visited=set()
            course_stack = deque()
            course_stack.append(course)
            while course_stack:
                current_course= course_stack.popleft()
                if current_course not in visited:
                    visited.add(current_course)
                    path.append(current_course)
                    
                if graph.get(current_course):
                    for node in graph[current_course]:
                        if node not in visited:
                            course_stack.append(node)
                if len(path) == len(courses):
                    return path
        return []

        

        
                
# @lc code=end

