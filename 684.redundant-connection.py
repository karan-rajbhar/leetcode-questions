#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

from typing import List
# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {v: -1 for v in range(1, len(edges) + 1)}

        def find(v):
            if parent[v] == -1:
                return v
            return find(parent[v])

        def union(u, v):
            u_root = find(u)
            v_root = find(v)
            if u_root == v_root:
                return True
            parent[u_root] = v_root
            return False

        for u, v in edges:
            if union(u, v):
                return [u, v]


# @lc code=end
