Approach 1:
  
''' In 1st Approach, we will count the Number of Nodes present inside the Linked-List.
Lastly, we will use another While Loop which will run till (N / 2) times.
And the Node where it will stop will be our Middle of LinkedList

'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      # N will store the number of Nodes present in the Linked List      
      n = 0   
      temp = head       # We always use a temp pointer so that our head pointer doesn't get lost
      while temp != None:   # we iterate, while temp pointer reaches the end of Linked List
        temp = temp.next    
        n += 1
        
      half = n // 2
      temp = head   # Again we Assign head to temp for thr second iteration
      
      while half:     # Second While Loop runs till half is greater than 0
        temp = temp.next
        half -= 1
        
      return temp
'''
T.C : O(N) { Two iterations are used }
S.C : O(1)
'''
    
Approach 2:
  
'''
In 2nd Approach, we don't need to count the Number of Nodes present inside the LinkedList
We will use Two Pointers - Slow and Fast
Slow will move with a Single Node every time
Fast will move with a speed double that of Slow, that is, by Moving Two Nodes everytime
When our Fast will be NULL or our Fast will be at the Last Node, then our Slow pointer will
'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        #  We will come out of the While Loop whenever we our Fast pointer becomes NULL or our Fast pointer is pointing to the Last Node
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            # At the end, our Slow pointer will be pointing to the Middle of the LinkedList
        return slow

'''
Time Complexity:  O(N) { Only a Single iteration is used }
Space Complexity: O(1)
'''
