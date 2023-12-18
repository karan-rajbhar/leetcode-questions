#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#
from collections import deque
from typing import List

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        visited= set(deadends)
        queue= deque()
        queue.append(['0000',0])

        while queue:
            lock , step = queue.popleft()
            if lock == target:
                return step
            
            for child in self.children(lock):
                if child not in visited:
                    visited.add(child)
                    queue.append([child,step+1])

        return -1        
    
    def children(self,lock):
        res=[]
        for i in range(4):
            x= int(lock[i])
            for d in (-1,1):
                y=(x+d)%10
                res.append(lock[:i]+str(y)+lock[i+1:])

        return res


# solution = Solution()
# print(solution.openLock(["0201","0101","0102","1212","2002"], "0202"))
        
# @lc code=end

