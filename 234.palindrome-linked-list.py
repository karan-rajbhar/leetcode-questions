#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        list_num=[]
        list_num.append(head.val)
        curr= head
        while True:
            if curr.next:
                curr=curr.next
                list_num.append(curr.val)
            else:
                break
                
        if len(list_num) ==2:
            if list_num[0] == list_num[1]:
                return True
            
            return False
        
        if len(list_num) %2==0:
            length=len(list_num)
            if list_num[0:(length//2)] == list_num[(length//2):length+1][::-1]:
                return True
            else:
                return False
        else:
            
            length=len(list_num)
            if list_num[0:(length//2)] == list_num[(length//2)+1:length+1][::-1]:
                return True
            else:
                return False
            
                
            
                
# @lc code=end

