#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        node_count=0

        
        while fast:
            fast=fast.next
            node_count+=1
        
        
        slow = head
        for i in range(0, (node_count//2)):
            slow=slow.next
        
        return slow
# @lc code=end

