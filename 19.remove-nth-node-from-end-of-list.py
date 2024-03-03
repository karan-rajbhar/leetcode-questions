#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next= head
        fast = slow = temp

        for _ in range(n):
            fast=fast.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next

        slow.next=slow.next.next

        return temp.next

# solution =  Solution()
# print(solution.removeNthFromEnd([1,2,3,4,5],2))
# @lc code=end

