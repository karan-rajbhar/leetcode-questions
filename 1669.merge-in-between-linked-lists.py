#
# @lc app=leetcode id=1669 lang=python3
#
# [1669] Merge In Between Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        
        temp = list1
        result= temp
        for _ in range(a-1):
            temp=temp.next

        dummy = ListNode(0,temp.next)   
        
        for _ in range(b-a+1):
            dummy=dummy.next
        
        temp.next= list2
        while temp.next:
            temp=temp.next
        
        temp.next= dummy.next

        return result        
# @lc code=end

