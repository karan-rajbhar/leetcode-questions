#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val==val:
            head=head.next
                
        prev=None
        curr=head
        while curr:
            if curr.val==val:
                if prev:
                    prev.next=curr.next
                else:
                    head=curr.next
            else:
                prev=curr
            
            curr=curr.next
                
        return head
        
# @lc code=end

