#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        # Calculate the length of the linked list
        length = 1
        curr = head
        while curr.next:
            length += 1
            curr = curr.next

        # Make the linked list circular
        curr.next = head

        # Find the new head after rotation
        for i in range(length - k % length):
            curr = curr.next

        # Set the new head and disconnect the circular reference
        result = curr.next
        curr.next = None

        return result                
# @lc code=end

