#
# @lc app=leetcode id=1171 lang=python3
#
# [1171] Remove Zero Sum Consecutive Nodes from Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        memo = { 0: dummy}
        pre_sum = 0

        while head:
            pre_sum +=head.val

            if pre_sum in memo:
                start = memo[pre_sum]
                temp = start
                temp_sum = pre_sum

                while temp != head:
                    temp = temp.next
                    temp_sum += temp.val

                    if temp != head:
                        memo.pop(temp_sum)
                
                start.next= head.next

            else:
                memo[pre_sum] = head

            head= head.next

        return dummy.next
        
# @lc code=end

