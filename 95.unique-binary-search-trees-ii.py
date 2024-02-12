#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
from typing import List, Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def generate(left, right):
            if left == right:
                return [TreeNode(left)]
            
            if left > right:
                return [None]
            
            result = []
            for val in range(left, right+1):
                for leftTree in generate(left, val-1):
                    for rightTree in generate(val+1,right):
                        root = TreeNode(val, leftTree, rightTree)
                        result.append(root)
            return result
            
        return generate(1,n)
        
# @lc code=end

