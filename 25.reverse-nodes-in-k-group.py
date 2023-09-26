#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
from typing import Optional


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        current = head
        for _ in range(k):
            if not current:
                return head
            current = current.next


        prev = None
        current = head
        
        for _ in range(k):
            next = current.next
            current.next = prev
            prev =current
            current = next

        head.next = self.reverseKGroup(current ,k)

        return prev

# l1 = ListNode(1)
# l2 = ListNode(2)
# l3 = ListNode(3)
# l4 = ListNode(4)
# l5 = ListNode(5)
# l6 = ListNode(6)
# l7 = ListNode(7)
# l8 = ListNode(8)
# l9 = ListNode(9)

# l1.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l5
# l5.next = l6
# l6.next = l7
# l7.next = l8
# l8.next = l9

# solution = Solution()
# result = solution.reverseKGroup(l1, k=2)


# while result:
#     print(result.val)
#     result = result.next

# @lc code=end
