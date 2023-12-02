#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
def print_list(node):
    print("Printing list: ", end='')
    while node:
        next_val = node.next.val if node.next else 'None'
        print(f"Node({node.val}, next={next_val})", end=' --> ')
        node = node.next
    print('None')  # for newline after printing all nodes


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        curr=head
        while curr:
            node=Node(curr.val,curr.next)
            curr.next=node
            if curr.next.next:
                curr=curr.next.next
            else:
                break
        curr=head
        
        while curr:
            if curr.random:
                curr.next.random=curr.random.next
            curr = curr.next.next
        
        second = curr = head.next
        while curr.next:
            head.next = curr.next    
            head = head.next
            curr.next = head.next
            curr = curr.next
        
        head.next = None
        # print_list(head)
        return second
                
# @lc code=end

