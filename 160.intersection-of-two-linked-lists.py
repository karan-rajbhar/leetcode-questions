#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        currA=headA
        currB=headB
        while currA is not currB:
            currA=headB if currA is None else currA.next
            currB=headA if currB is None else currB.next
            
        return currA
        
# @lc code=end

