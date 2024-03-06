#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow = head
        if head.next is not None:
            fast =head.next
        else:
            return False
        while fast and fast.next:
            if fast == slow:
                return True
            slow= slow.next
            fast=fast.next.next
        
        return False

# @lc code=end

