#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        queue = []
        for list in lists:
            temp_node=list
            while temp_node:
                heapq.heappush(queue,(temp_node.val, temp_node))
                temp_node=temp_node.next

        new_head = ListNode(0)
        result = new_head
        while queue:
            _,new_head.next=heapq.heappop(queue)
            new_head = new_head.next
        new_head.next=None
        return result.next
        
# @lc code=end

