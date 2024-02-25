#
# @lc app=leetcode id=2709 lang=python3
#
# [2709] Greatest Common Divisor Traversal
#

# @lc code=start
import math
from typing import List
from collections import deque

class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
    
        number_set = {i for i in range(len(nums))}
        visited = set({0})
        queue = deque()
        queue.append(0)
        unvisited = number_set - visited
        
        while queue:
            i = queue.popleft()
            for j in unvisited:
                if math.gcd(nums[i], nums[j]) > 1:
                    visited.add(j)
                    queue.append(j)
                    unvisited = number_set - visited
            
        if visited == number_set:
            return True
        return False


# print(Solution().canTraverseAllPairs([3,9,5]))
# print(Solution().canTraverseAllPairs([4, 6, 15, 35]))
# print(Solution().canTraverseAllPairs([2, 3, 6]))
# print(Solution().canTraverseAllPairs([3, 9, 5]))
# print(Solution().canTraverseAllPairs([4,3,12,8]))
# print(Solution().canTraverseAllPairs([26,42,45,30,35]))
# @lc code=end
