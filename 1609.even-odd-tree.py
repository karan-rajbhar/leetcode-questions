#
# @lc app=leetcode id=1609 lang=python3
#
# [1609] Even Odd Tree
#

# @lc code=start
# Definition for a binary tree node.
from collections import defaultdict,deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level_dict=defaultdict(list)
        queue = deque([(root,0)])

        while queue:
            node,count = queue.popleft()

            if node is None:
                continue
            
            level_dict[count].append(node.val)

            queue.append((node.left , count+1))
            queue.append((node.right , count+1))

        for level , values in level_dict.items():
            for i, value in enumerate(values):
                if level%2 == 0:
                    if value%2 == 0:
                        return False
                    if i>0 and value<=values[i-1]:
                        return False
                else:
                    if value%2 != 0:
                        return False
                    if i>0 and value>=values[i-1]:
                        return False
                
        return True
        
# @lc code=end

