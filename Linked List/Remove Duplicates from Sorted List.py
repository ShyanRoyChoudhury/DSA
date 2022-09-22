# Approach 1: Using recursion:

class Solution(object):
    def deleteDuplicates(self, head):
        
        if not head or not head.next:
            return head
          
        """ We ask Recursion to remove all duplicates starting from Head's next"""
        newHead = self.deleteDuplicates(head.next)
        # If the values pointed by Head and newHead(given to us by Recursion) are same, 
        # we don't need to add Head into our new Sorted LinkedList without any Duplicates, so we directly return newHead
        if head.val == newHead.val:
            return newHead
        else:
            head.next = newHead   # Otherwise, their values don't match, so we need to include Head into our Linkedlist
            return head
          
    """
        Time Complexity:  O(N) { N is the Number of Nodes present in Linkedlist }
        Space Complexity: O(N) { Auxillary Recursive Stack Space }


    """
          
# Approach 2: Using iteration
class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
      
        temp = head
        while temp.next is not None:
            if temp.val == temp.next.val:
                Del = temp.next   # we store temp's next Node into a del variable
                temp.next = Del.next    # we shift temp's next pointer to Del.next
                del Del
            # But our Temp Pointer moves only when values pointed by Temp & Temp's Next are different
            else:
                temp = temp.next
          
        return head   # at the end we return head of the linked list
    
    
    """
    Time Complexity:  O(N) { N is the Number of Nodes present in Linkedlist }
    Space Complexity: O(1)

    """
