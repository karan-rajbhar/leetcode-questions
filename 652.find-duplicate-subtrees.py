#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtree=defaultdict(list)
        def dfs(node):
            if node is None:
                return "null"
            
            s=",".join([str(node.val),dfs(node.left),dfs(node.right)])
            
            if len(subtree[s]) ==1:
                res.append(node)
            subtree[s].append(node)
            
            return s
        res=[]
        
        dfs(root)
        
        return res
# @lc code=end

