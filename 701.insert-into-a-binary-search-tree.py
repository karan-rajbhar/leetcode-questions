#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        def recursive(node,val):
            if node.val > val:
                if node.left is None:
                    node.left = TreeNode(val)
                    return
                else:
                    recursive(node.left,val)
            else:
                if node.right is None:
                    node.right= TreeNode(val)
                    return
                else:
                    recursive(node.right,val)

        recursive(root,val)
        return root
        
# @lc code=end

