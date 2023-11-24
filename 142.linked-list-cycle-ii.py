#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        slow=head
        entry=head
        fast=head
        
        
        while fast is not None and slow.next is not None and fast.next is not None:
            slow=slow.next
            if fast.next is not None:
                fast=fast.next.next
            if slow==fast:
                while slow is not entry:
                    slow=slow.next
                    entry=entry.next
                return entry
            
        return None        
# @lc code=end

