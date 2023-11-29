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


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head.next is None:
            return head
        
        result_node=Node(0)
        result_node_head=result_node
        curr=head
        while curr:
            if curr.child:
                child=curr.child
                flatted = self.flatten(child)
                

                node=Node(curr.val,curr,flatted)
                print("printing flatted")
                print_list(flatted)
                result_node.next=curr
                node.prev=result_node
                
                result_node.next=node
                
                while result_node.next:
                    result_node=result_node.next
                
                curr=curr.next
            else:
                curr.prev=result_node
                result_node.next=curr
                result_node=result_node.next
                curr=curr.next
                
            print("printing Result")
            result_node_head.next.prev=None
            print_list(result_node_head.next)

            
        return result_node_head.next
# Creating the multilevel linked list
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
node12 = Node(12)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

node2.child = node7
node7.next = node8
node8.next = node9
node9.next = node10

node8.child = node11
node11.next = node12

solution = Solution()
solution.flatten(node1)


# @lc code=end


