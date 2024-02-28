#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None

        self.longest = root.val
        self.length=0
        self.recursive(root,0)

        return self.longest
    def recursive(self,node,count):    
        if node is None:
            return
        if count > self.length:                
            self.longest = node.val
            self.length=count

        self.recursive(node.left, count+1)
        self.recursive(node.right, count+1)        
# @lc code=end

