#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        total = 0
        queue = deque([root])
        while queue:
            node = queue.popleft()

            if node is None:
                continue
            
            if node.val >= low and node.val <= high:
                total = total+node.val
            
            queue.append(node.left)
            queue.append(node.right)

        return total
        
# @lc code=end

