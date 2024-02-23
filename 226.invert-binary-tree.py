#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
            
        if root.left and root.right:
            temp = root.left
            root.left = root.right
            root.right= temp
            
        elif root.left and root.right is None:
            root.right=root.left
            root.left =None
        else:
            root.left= root.right
            root.right=None

        self.invertTree(root.left)
        self.invertTree(root.right)

        return  root
        
# @lc code=end

