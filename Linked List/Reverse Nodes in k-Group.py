# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
n Approach - 1, we will be using Extra Space of Recursive Stack to Reverse Nodes in Groups of K
In this solution, we will be Reversing Nodes in groups of K and ask our Recursive function to do rest of the Task.
Our Base Case will be when our head becomes NULL or our head is at the Last Node, in that case, we will simply return head without moving further
After Recursive function gives us our newHead, we will swap the Nodes from Start Pointer to End Pointer using our Iterative version of Reversing a Linked List


"""
class Solution:
    def reverseKGroup(self, head, k):

        def reverse(start, end):

            prev = None
            cur = start

            while prev != end:
                nextNode = cur.next # saved
                # break cur's next pointer
                cur.next = prev
                # update the prev pointer
                prev = cur
                # update the cur pointer
                cur = nextNode

        # Check if the head is None or it's next is None in that case we had to return Head
        if not head or k == 1 or not head.next:
            return head

        # Else create two Dummy nodes , both of them will point to head
        start, end = head, head

        # here inc is the loop control variable which will keep hold on the loop termination condition
        inc = k-1

        while inc > 0:
            end = end.next
            inc -= 1
            if not end: # alternate: if end is None:
                return head


        # Again Call the main ReversekGroup Function with value of end.next
        node = self.reverseKGroup(end.next, k)
        # call the reverse node function
        reverse(start, end)
        # Make start.next = node to connect the user done reversal with the reverse function output 
        start.next = node

        return end



"""
Hypothesis of reverseKGroup:
return ll with reverse k grp

reverse() -> API DONE

Base case:
if k* itr.next == None:     |   len(rem_ll) < k
    return head

Induction:
each time reverse k grps, inc by k times

Time  Complexity: O(N)
Space Complexity: O(N / K) { Recursive Stack Space }

"""
""" APPROACH 2: USING ITERATION
we will NOT be using any extra Recursive Stack Space
To save space, we will use be using iterative approach to Reverse Nodes in Groups of K
Instead of using Start, here we will be using beforeStart which points to the Node before Start Pointer
We also need to store the End's Next in temp variable
After reversing, we just have to make:
a) beforeStart -> next = End
b) Start -> next = temp
Move beforeStart to Start & end to temp for next set of reversals
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(start, end):
            prev = None
            cur = start
            nextNode = start.next
            
            while prev != end:
                cur.next = prev
                prev = cur
                cur = nextNode
                
                if nextNode is not None:
                    nextNode = nextNode.next
                    
        if k ==1 or not head or not head.next:
            return head
        
        dummy = ListNode(-1) #creating a dummy to assign its next to head
        dummy.next = head
        beforeStart = dummy 
        
        end = head
        i = 0   # iterator to keep track of no. of nodes traversed
        
        while end is not None:
            i += 1
            if i%k == 0:
                start = beforeStart.next    # start of the node
                temp = end.next # temp stores the end.next since we lose the connection during reversal
            
                reverse(start, end) #function to reverse the k group
                
                # restoring the connections of reverse group to the ll
                beforeStart.next = end #  After reversing is done, beforeStart's next should now point to End pointer
                start.next = temp   #  Start's next should point to temp(intial End's Next)
                
                # After tat, beforeStart should be moved to the place of Start Pointer

                beforeStart = start
                end = temp
            else:
                # Else if we haven't covered the LinkedList of Length K, we make End move to it's Next Node
                end = end.next
        # At the end, we return Dummy's Next which will be our new head after reversing all the nodes in k group        
        return dummy.next
