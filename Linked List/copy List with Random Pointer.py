"""
  In Approach - 2,  Using no extra spaces
    
   we will not be using a extra Map to store the copy of every Node from the Original LinkedList. Instead, we will be modifying the existing connections only.
   For every original Node, we will make it's Next pointer point to it's Deep Copy.
   And it's Deep Copy Next pointer should point to Original Node's Next.
   For example - A(Original Node) , A'' (Deep Copy Of A) , A Next --> B
   After modification, the LinkedList will look like:
   A Next --> A'' ;
   A'' Next -- B ;
   To clarify further, please watch the YouTube Video. This modfications will help us to get the random pointers of every original node very easily.

"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        temp = head
        while temp: #creating copies
            q = temp.next
            new_node = ListNode(temp.val)
            temp.next = new_node
            new_node.next = q

            temp = q

        temp = head

        while temp: # creating random connections
            if temp.random is None:
                temp.next.random = None
            else:
                temp.next.random = temp.random.next
            temp = temp.next.next

        original = head
        copy = head.next
        new_head = copy

        while original:
            original.next = original.next.next
            if copy.next is not None:
                copy.next = copy.next.next
            else:
                copy.next = None
            
            original = original.next
            copy = copy.next
        
        return new_head
      
      
"""
T.C: O(N)
S.C: O(1)
"""
