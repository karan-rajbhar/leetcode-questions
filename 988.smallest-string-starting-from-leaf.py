#
# @lc app=leetcode id=988 lang=python3
#
# [988] Smallest String Starting From Leaf
#

# @lc code=start
# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """

        stack=[(root,"")]
        smallest_string=""

        while stack:
            node , current_string= stack.pop()
            if node is None:
                continue
            current_string = chr(97+node.val)+current_string
            if node.left is None and node.right is None:
                if smallest_string == "":
                    smallest_string = current_string
                else:
                    smallest_string = min(smallest_string , current_string)


            stack.append((node.left,current_string))
            stack.append((node.right,current_string))

        return smallest_string
        
# @lc code=end

