"""
To check if the LinkedList is Palindrome or Not, firstly, we need to reach the Middle of the LinkedList using our Slow and Fast pointers approach.
After that, Slow pointer points to the Node just before the Middle of the Linked-List.
We reverse the LinkedList from Middle of the Linkedlist.
And then we have 2 pointers - Start & Mid. Mid points to Middle of the LinkedList(now reversed) & Start point to the Head of the LinkedList.
Before returning, we revert the same Linkedlist.

"""

class Solution:
    def reverse(self, head):        #   reverse function to reverse the linked list after mid
            prev = None
            cur = head
            nextNode = cur.next
            
            while cur!=None:
                cur.next = prev
                prev = cur
                cur = nextNode
                
                if nextNode!=None:
                    nextNode = nextNode.next
                    
            return prev
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head  or not head.next:
            return head
        slow = head
        fast = head
        """
         We need Slow to point to a Node just before the Middle-most Node of the LinkedList
        That's why we make Fast move to the Second Last Node of the LinkedList only

        """
        while fast.next!= None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next
        
        """
        Slow pointer is now at the Node just before Middle Of the LinkedList
        We need to reverse the LinkedList from the Middle Of the LinkedList,that is, Slow's Next Node
         We need to attach the Reversed List into Slow's Next

        """
        start = head
        slow.next = self.reverse(slow.next)
        mid = slow.next
        """
        After reversing, we will check if the LinkedList is Palindrome or not using 2 pointers - Start and Mid
        Start will begin from Head and Mid will start from Slow's Next
        If at any moment, there's value doesn't match, we can directly return false
        Otherwise, we will keep moving them. If at any moment, Mid becomes NULL, it means the LinkedList is Palindrome, so before moving, we again make the Original Connections and return true

        """
        
        while mid != None:
            if start.val != mid.val: return False    # If the Value pointed by Mid and Start are not same, then the LinkedList is not Palindrome
            
            mid = mid.next
            start = start.next
        #slow.next = self.reversal(slow.next)
        
        return True
    
"""
Time Complexity:  O(N)
Space Complexity: O(1)


"""
