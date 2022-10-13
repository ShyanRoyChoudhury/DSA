"""
Approach 1: Using map(using extra spaces)

In this question, we have been given a Linked-List which has two pointers:
                    a) Next Pointer --> Pointing to the Next Node of the Linked-List
                    b) Random Pointer --> Points to any Random Node of the LinkedList, even NULL

    We need to make a Deep Copy of LinkedList. Deep Copy refers that we need to actually copy the LinkedList
    We need to make the Deep Copy such that the Random Pointers of our new copied LinkedList should point to the Nodes where there copies were pointing initally.
        For example - If A(Given Node) A'(New Copied Node) & A's Random pointed to B initally
                        A's random -> B

    To make such connection possible, we will use an -Map which maps A with A' , B with B' and so on.


"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # We will store node and their deep copies inside Map m
        m,zero = dict(),Node(0)

        # curr is used to iterate over the given LinkedList

        cur,copy = head,zero

# In 1st iteration, we create copies and store the Nodes and their Copies as Key-Value pair inside our Map M

        while cur:
            # We create a Copy of the Given Node using curr's Value
            copy.next = Node(cur.val)

            # We store the Node as well it's copy inside our Map M
            m[cur] = copy.next
            cur,copy = cur.next,copy.next
        # We again reinitialise Temp to Head to iterate again
        cur,copy = head,zero.next

        # In 2nd iteration, we will make connections of the copies stored in Map M
        while cur:
            """
            M[curr] will give us the Copy Node of curr
            M[curr -> Next] will give us th Copy Node of curr's Next
            Copied Node's Next should point to the Copied Node of curr's Next

            """
            copy.random = m[cur.random]  if cur.random else None
            cur,copy = cur.next,copy.next


        #  At the end, we return M[head] which is actually Head of our Copied LinkedList
        return zero.next
      
 """
Time Complexity:  O(N)
Space Complexity: O(N)


"""





"""
  In Approach - 2,  Using no extra spaces (BETTER SOLUTION)
    
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
        while temp: #creating copies and connecting to original list
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

        while original: # separing the copy list from original list
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
