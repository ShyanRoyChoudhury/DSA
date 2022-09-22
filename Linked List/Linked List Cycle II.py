"""
This question is exactly similar to the Linked List Cycle I. Only difference is that in this problem we need to find the Node from where the cycle begins.
But our apporach remains same. We will use 2 pointers - slow & fast where fast moves with a speed double the speed of slow.
If slow and fast meet, then the LinkedList definetly contains a Cycle.
To find the starting point of tat Cycle, we will use 2 pointers again- ptr1 & ptr2
Ptr1 will start from the Head of the LinkedList, while ptr2 will start from the Slow pointer
Both ptr1 & ptr2 will move at the same time. The point where ptr1 & ptr2 meets is the Required Node
"""

class Solution(object):
    def detectCycle(self, head):
      
      #  Intially, Slow & Fast pointer both will start from Head of the LinkedList

      fast = head
      slow = head
      
      while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:  break     # If Slow & Fast pointer meets, then there's a Cycle in the LinkedList

          
      if fast is None or fast.next is None:   # If our Fast becomes NULL or our Fast's Next Node is NULL, it means there's No Loop in the LinkedList
        return None
      
      ptr1 = head
      ptr2 = slow
      
      while ptr1 == ptr2:
        ptr1 = ptr1.next    # Ptr1 & Ptr2 moves with the same speed
        ptr2 = ptr2.next
        
      return ptr1   # At the end, both Ptr1 or Ptr2 will point to the starting Node of the LinkedList Cycle / Loop
