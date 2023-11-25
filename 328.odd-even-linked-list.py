#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # def __str__ (self):
    #     return self.val
        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        count=1
        odd=ListNode(val=0)
        even=ListNode(val=0)
        odd_head=odd
        even_head=even
        curr=head
        while True:
            if count % 2==0:
                node=ListNode(val=curr.val)
                even.next=node
                even=node
            else:
                node=ListNode(val=curr.val)
                odd.next=node
                odd=node
            if curr.next:
                curr=curr.next
            else:
                break
            count+=1
        
                    
        odd.next=even_head.next
        return odd_head.next

    def oddEvenList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        odd=head
        even=head.next
        even_head=even
        
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        
        odd.next=even_head
        return head
                
# @lc code=end

