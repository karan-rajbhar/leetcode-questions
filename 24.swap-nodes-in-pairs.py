#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#


# @lc code=start
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev and prev.next and prev.next.next:
            # Node to be swapped
            first = head
            second = head.next
            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first

            #Move Pointers for the next iteration
            prev = first
            head = first.next
            
        return dummy.next


# l1 = ListNode(1)
# l2 = ListNode(2)
# l3 = ListNode(3)

# l1.next = l2
# l2.next = l3

# solution = Solution()
# result = solution.swapPairs(l1)

# while(result):
#     print(result.val)
#     result=result.next
# @lc code=end
