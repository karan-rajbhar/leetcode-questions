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

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None or head.next is None:
            return False
        
        if head.next.next is None:
            return False
        
        slow=head
        fast=head.next
        
        while slow.next is not None and fast.next is not None:
            if slow == fast:
                return True
            
            slow=slow.next
            if fast.next.next is None:
                return False
            fast=fast.next.next
        
        return False
                
# @lc code=end

