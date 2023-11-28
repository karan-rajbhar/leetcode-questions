#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_node=ListNode(0)
        result_node_head=result_node
        curr_l1=l1
        curr_l2=l2
        carry=0
        result=0
        while curr_l1 or curr_l2:
            if curr_l1 and curr_l2:
                result=curr_l1.val+curr_l2.val+carry    
            elif curr_l1:
                result=curr_l1.val+carry
            
            elif curr_l2:
                result=curr_l2.val+carry
            
            if result>=10:
                carry=result//10
                result=result-10
            else:
                carry=0
            node=ListNode(result)
            result_node.next=node
            result_node=result_node.next
            
            if curr_l1 and curr_l1.next:
                curr_l1=curr_l1.next
            else:
                curr_l1=None
                
            if curr_l2 and curr_l2.next:
                curr_l2=curr_l2.next
            else:
                curr_l2=None
            
        if carry !=0:
            node=ListNode(carry)
            result_node.next=node
        
        return result_node_head.next
            
            
                    
# @lc code=end

