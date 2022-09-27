"""
In Approach - 1, we will use iteration to remove the occurrences of val(key) from the given LinkedList
We will create a Dummy Node to keep track of our new LinkedList after removing all occurrences from the given Linkedlist.
We require another point Tail to traverse the LinkedList. Tail initally points to Dummy
We move Tail till Tail is not Equal to NULL OR Tail's Next is Not Equal to NULL.
If Tail's Value is equal to Tail's Next Node's Value, we perform Deletion
Otherwise, we keep moving Tail to Next Node

"""
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head   # if head is None , then we dierectly Return it
        
        dummy = ListNode(-1)  # We create Dummy to keep track of the Linkedlist after removing all occurrences of Val
        dummy.next = head
        
        tail = dummy  # Tail initially points to head
        
        while tail != None and tail.next != None:
            if tail.next.val == val:
                temp = tail.next  # We take new node temp as tail's next node
                tail.next = temp.next
                del temp  # And then delete temp
                
            else: # Else  the values are not equal , so we make tail move to tail's next node

                tail = tail.next  
                
        return dummy.next
"""
Time Complexity:  O(N)
Space Complexity: O(1)

"""


"""
In Approach - 2, we will use Recursion to remove the occurrences of val(key) from the given LinkedList
Unlike in iteration, we will ask Recursion to do most of the Task. We will only do a small Task
We will ask recursion to remove all occurrences of Val from LinkedList starting from Head's Next Node and return the newHead
After that we will check if Head's Val is equal to newHead or Not.
If true, we shouldn't add Head into our LinkedList so we return newHead
Else, Value is not equal to Val(Key), so we add Head's Next to newHead and return head

"""
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        # we ask Recursion to do the task and remove all the occurences of Val(Key) starting from Head's Next Node
        head.next = self.removeElements(head.next, val)
        
        if head.val == val: # if Head's Value is equal to Val
            ans = head.next # we store head's next in ans pointer
            del head
            return ans
        
        else:
            return head
          
"""
Time Complexity:  O(N)
Space Complexity: O(N) { Auxillary Stack Space }

"""
