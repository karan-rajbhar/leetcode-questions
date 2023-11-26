#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start
class Node:
    def __init__(self,val=0,next=None,prev=None):
        self.val=val
        self.next=next
        self.prev=prev
    def __str__(self):
        values=[self.val]
        curr=self.next
        while curr.next is not None:
            values.append(curr.val)
            curr=curr.next
            
        return str(values)

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        
    def get(self, index: int) -> int:
        curr=self.head
        if index < 0 or index >=self.size:
            return -1
        
        if self.head is None:
            return -1
        
        curr=self.head
        
        for i in range(index):
            curr=curr.next
        
        return curr.val
                
    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head=Node(val)
            self.size+=1    
        else:
            node= Node(val=val)
            node.next=self.head
            self.head.prev=node
            self.head=node
            self.size+=1    
    
        
        
    def addAtTail(self, val: int) -> None:
        curr=self.head
        if curr is None:
            self.head=Node(val)
        else:            
            while curr.next is not None:         
                curr=curr.next
            node=Node(val)
            node.prev=curr
            curr.next= node
        self.size+=1
            
    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index >self.size:
            return
        
        if index ==0:
            self.addAtHead(val)
        else:
            curr=self.head
            for i in range(index-1):
                curr=curr.next
            node = Node(val)
            node.next=curr.next
            node.prev=curr
            curr.next=node
            self.size+=1
        
    def deleteAtIndex(self, index: int) -> None:
        print(index)
        if index<0 or index >= self.size:
            return

        curr=self.head
        
        if index ==0:
            self.head=curr.next
        else:
            for i in range(index-1):
                curr=curr.next
            if curr.next.next is not None and curr.next.prev:
                curr.next=curr.next.next
                curr.next.prev=curr
            else:
                curr.next=None
        self.size -=1

                
                

        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)               

        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

