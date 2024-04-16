#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth == 1:
            return TreeNode(val = val , left = root , right = None)

        
        stack=[(root, 1)]

        while stack :
            node , current_depth = stack.pop()

            if node is None:
                continue

            if current_depth +1 == depth:
                node.left = TreeNode(val = val , left = node.left , right=None)
                node.right = TreeNode(val = val , left = None , right=node.right)

            stack.append((node.left , current_depth+1))
            stack.append((node.right , current_depth+1))    

        return root
        
# @lc code=end

