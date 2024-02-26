#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    #Recursive solution
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if p is None and q is None:
    #         return True 

    #     if p is None or q is None:
    #         return False

    #     if p.val != q.val:
    #         return False


    #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)        
    
    #Solution using queue in iterative way
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((p,q))

        
        while queue:
            p,q = queue.popleft()

            if p is None and q is None:
                continue 

            elif p is None or q is None:
                return False

            elif p.val != q.val:
                return False
            else:
                queue.append((p.left,q.left))
                queue.append((p.right,q.right))
        
        return True
# @lc code=end

