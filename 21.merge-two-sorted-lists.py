#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr_list1=list1
        curr_list2=list2
        merge_node=ListNode(0)
        merge_node_head=merge_node
        while curr_list1 and curr_list2 :
            if curr_list1.val > curr_list2.val:
                merge_node.next=curr_list2
                merge_node=merge_node.next
                curr_list2=curr_list2.next
            else:
                merge_node.next=curr_list1
                merge_node=merge_node.next
                curr_list1=curr_list1.next
                
        if curr_list1 :
            merge_node.next=curr_list1
        if curr_list2 :
            merge_node.next=curr_list2
        
        return merge_node_head.next
                
            
            
        
# @lc code=end

