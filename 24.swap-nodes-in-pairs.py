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

        temp = head.next
        head.next = self.swapPairs(temp.next)
        temp.next = head
        
        return temp
    


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
