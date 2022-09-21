# Approach 1: Using Recursion
"""
We will be using the Same Existing Nodes only to create the Merged LinkedList

In the Recursive Solution, We will do the small task and ask recursion to do rest of the task
This means, we will compare the values of both List1 & List2 and whichever value is smaller, we will take that Node as a part of our Sorted LinkedList
After that, we will ask Recursion to do rest of the task & the Sorted List returned by Recursion will be attached to our Selected Node's Next

"""
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def merge(l1, l2):
            if not l1:  # if list 1 is not there, then simply return list 2
                return l2
            if not l2:  # if list 2 is not there, then simply return list 1
                return l1
            """
             If both are Non-NULLS, we compare the value pointed at by l1 and l2
             If l1's value is smaller, we will choose l2
             Else we will choose l2
             If the values are same, we can choose from either List1 or List2

             If l1's value is smaller than l2
            """
            if l1.val<l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            else:
                l2.next = merge(l1, l2.next)
                return l2
            
        return merge(list1, list2)
        '''
                 We pick the node pointed by l1 and ask recursion to do rest of the task
                 We attach the sorted list to L1's Next and return l1
    
                We pick the node pointed by l2 and ask recursion to do rest of the task
                We attach the sorted list to L2's Next and return l1
               
        '''

        '''
        Time Complexity:  O(M + N) { M is the Number of Nodes in List1 , N is the Number of Nodes in List2 }

        Space Complexity: O(M + N) { Auxillary Stack Space }
        '''
 #  Approach 2: Using Iteration
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans = ListNode(-1)
        tail = ans
        
        while list1 is not None and list2 is not None:
            if list1.val<list2.val:
                tail.next = list1
                tail = list1
                list1 = list1.next
                
            else:
                tail.next = list2
                tail = list2
                list2 = list2.next
        
        if not list1:         # Check if First list is not there, then return list2
            tail.next = list2
        else:
            tail.next = list1   # Check if second list is not there, then return list1
            
        return ans.next   # ans.head is dummy node, merged linked list starts from ans.head
