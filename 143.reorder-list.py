#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # Helper function to reverse a linked list
        def reverse_node(node):
            prev = None
            current = node
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev

        # Count the number of nodes in the linked list
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count += 1

        # Move the fast pointer to the middle of the linked list
        fast = head
        for _ in range(0, count // 2):
            fast = fast.next

        # Reverse the second half of the linked list
        fast = reverse_node(fast)

        # Merge the first and second halves
        slow = head
        while fast and fast.next:
            temp_fast = fast.next
            temp_slow = slow.next

            # Merge the nodes
            fast.next = slow.next
            slow.next = fast

            # Move the pointers
            fast = temp_fast
            slow = temp_slow

                 


        
# @lc code=end

