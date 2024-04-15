#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        root_leafs=[]

        stack = [(root,[])]

        while stack:
            
            
            node , prev_vals = stack.pop()
            
            if not node:
                continue
            
            
            if node.left is None and node.right is None:
                prev_vals.append(node.val)
                root_leafs.append(prev_vals)
                continue

            prev_vals.append(node.val)

            stack.append((node.left , prev_vals[:]))
            stack.append((node.right , prev_vals[:]))
            
        total = 0

        for array in root_leafs:
            total += int("".join(str(x) for x in array))


        return total        
        

# @lc code=end

