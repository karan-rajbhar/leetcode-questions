#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

from typing import Optional

class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __str__(self):
        return f"Node({self.val}, prev={self.prev.val if self.prev else None}, next={self.next.val if self.next else None})"

def print_list(node):
    print("Printing list: ", end='')
    while node:
        prev_val = node.prev.val if node.prev else 'None'
        next_val = node.next.val if node.next else 'None'
        print(f"Node({node.val}, prev={prev_val}, next={next_val})", end=' --> ')
        node = node.next
    print('None')  # for newline after printing all nodes

def is_valid_doubly_linked_list(head):
    if not head:
        return "Empty list is considered as a valid doubly linked list."

    # Traverse from head to tail
    prev = None
    curr = head
    while curr:
        if prev != curr.prev:
            return "Prev pointer is not correctly set."
        prev = curr
        curr = curr.next

    tail = prev

    # Traverse from tail to head
    next_node = None
    curr = tail
    while curr:
        if next_node != curr.next:
            return "Next pointer is not correctly set."
        next_node = curr
        curr = curr.prev

    if head != next_node:
        return "Can't reach the original head from the tail."

    return "It's a valid doubly linked list."

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None :
            return head
        
        result_node=Node(0)
        result_node_head=result_node
        curr=head
        while curr:
            if curr.child:
                child=curr.child
                flatted = self.flatten(child)
                next_curr=curr.next
                curr.next=flatted
                curr.child=None
                flatted.prev=curr
                result_node.next=curr
                result_node.child=None
                while result_node.next:
                    result_node.child=None
                    result_node=result_node.next
                curr=next_curr
            else:
                curr.prev=result_node
                curr.child=None
                result_node.next=curr
                result_node=result_node.next
                curr=curr.next
                            
        result_node_head.next.prev=None
        # print_list(result_node_head.next)
        # message = is_valid_doubly_linked_list(result_node_head.next)
        # print(message)
        return result_node_head.next


# # Creating the nodes
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# node6 = Node(6)
# node7 = Node(7)
# node8 = Node(8)
# node9 = Node(9)
# node10 = Node(10)
# node11 = Node(11)
# node12 = Node(12)

# # Linking the nodes
# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2
# node3.next = node4
# node4.prev = node3
# node4.next = node5
# node5.prev = node4
# node5.next = node6
# node6.prev = node5

# node3.child = node7
# node7.next = node8
# node8.prev = node7
# node8.next = node9
# node9.prev = node8
# node9.next = node10
# node10.prev = node9

# node8.child = node11
# node11.next = node12
# node12.prev = node11
# # print_list(node1)
# solution = Solution()
# solution.flatten(node1)



# @lc code=end


