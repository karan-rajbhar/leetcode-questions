#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        stack=[]
        curr= root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            result.append(curr.val)
            curr=curr.right
        
        return result
    
    
    
    
    
    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def inorder(node,result):
            if not node:
                return result 
            
            
            inorder(node.left,result)
            result.append(node.val)
            inorder(node.right,result)
            
            return result
        inorder(root,result)     
        
        return result
        
# @lc code=end

