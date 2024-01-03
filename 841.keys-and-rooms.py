#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

from typing import List

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys=[]
        keys.append(rooms[0])
        visited=set()
        visited.add(0)
        while keys:
            current_keys=keys.pop()
            for key in current_keys:
                if key in visited:
                    continue
                keys.append(rooms[key])
                visited.add(key)
        
        if len(visited) == len(rooms):
            return True
        
        return False
        
# @lc code=end

