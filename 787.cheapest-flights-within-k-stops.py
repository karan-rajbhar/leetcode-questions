#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # Initialize the cost to each city as infinity, except for the source city
        cost = [float('inf')] * n
        cost[src] = 0

        # Relax the edges K+1 times
        for _ in range(K+1):
            temp = list(cost)
            for u, v, w in flights:
                temp[v] = min(temp[v], cost[u] + w)
            cost = temp
        
        # If the cost to the destination city is still infinity, return -1
        if cost[dst] == float('inf'):
            return -1
        else:
            return cost [dst]


# solution = Solution()
# print(solution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)) # 200