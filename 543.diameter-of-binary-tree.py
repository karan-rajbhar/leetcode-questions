#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

from collections import deque
from typing import Optional
# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        memoization = {}
        def height(node):
            if node is None:
                return 0
            if node in memoization:
                return memoization[node]
            memoization[node]=1 + max(height(node.left),height(node.right))
            return memoization[node]
        longest_path=0
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node is None:
                continue
            diameter = height(node.left)+height(node.right)

            if diameter > longest_path:
                longest_path = diameter

            queue.append(node.left)
            queue.append(node.right)
        
        return longest_path
        
# @lc code=end

