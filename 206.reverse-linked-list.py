#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Iterative
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=None
        
        while head:
            temp=head.next
            head.next=node
            node=head
            head=temp
        
        return node
    
    #recursive
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node        
        
solution = Solution()
solution.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))

# @lc code=end

