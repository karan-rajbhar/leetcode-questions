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
            values = level_dict[count]

            if len(values) > 0:
                if count%2 == 0:
                    if node.val <= values.pop() or node.val%2 == 0:
                        return False
                else:
                    if node.val >= values.pop() or node.val%2 == 1:
                        return False
            else:
                if count %2 ==0:
                    if node.val %2==0:
                        return False
                else:
                    if node.val %2 ==1:
                        return False
                    
            level_dict[count].append(node.val)

            queue.append((node.left , count+1))
            queue.append((node.right , count+1))
        
        return True        
# @lc code=end

