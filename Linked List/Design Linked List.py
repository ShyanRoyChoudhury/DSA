class node2:                    # creating a node with reference passed to it initially
    def __init__(self,val):
        self.val = val
        self.next = None
        
class MyLinkedList(object):

    def __init__(self):
        self.head = None
        
    def getLength(self):      # function to find the length of Linked List
        count = 0
        iterator = self.head
        while iterator:
            count+=1
            iterator = iterator.next
        return count

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        length = self.getLength()
        if index < 0 or index >= length:
            return -1
        elif index == 0:
            return self.head.val
        else:
            count = 0
            iterator = self.head
            while iterator.next:
                count += 1
                if count == index:
                    return iterator.next.val
                    break
                iterator = iterator.next

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = node2(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = node2(val)
        if self.head is None:
            self.head = new_node
            return
        
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        
        iterator.next = new_node

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        length = self.getLength()
        if index < 0 or index > length:
            return 'Invalid index'
        elif index == 0:
            new_node = node2(val)
            new_node.next = self.head
            self.head = new_node
        else:
            iterator = self.head
            count = 0
            while iterator:
                count += 1
                
                if count == index:
                    new_node = node2(val)
                    new_node.next = iterator.next
                    iterator.next = new_node
                
                iterator = iterator.next

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        iterator = self.head
        length = self.getLength()
        if index < 0 or index > length:
            return 'Invalid index'
        elif index == 0:
            self.head = iterator.next
        else:
            count = 0
            while iterator.next:
                count += 1
                if count == index:
                    iterator.next = iterator.next.next
                    break
                iterator = iterator.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
