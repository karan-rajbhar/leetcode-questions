#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

# @lc code=start
from collections import defaultdict
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        def dfs(current_node, visited):
            if current_node == destination:
                return True
            
            visited.add(current_node)
            
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    if dfs(neighbor, visited):
                        return True
            
            return False
            
        if not edges:
            return True

        graph=defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        
        visited = set()
        return dfs(source, visited)


                
# @lc code=end

