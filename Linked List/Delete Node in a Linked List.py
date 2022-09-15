class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next:  #checking whether next node is None or not
          # if it is not None then make its value  copy to current Node
          # In this Approach We are not using any temporary Node to copy the data
          node.val = node.next.val
          if node.next.next == None:
            node.next = None
            return
          node = node.next  # shift the node pointing to current to current->next in each iteration
          
          
'''
Time Complexity:  O(1)
Space Complexity: O(1)

'''
