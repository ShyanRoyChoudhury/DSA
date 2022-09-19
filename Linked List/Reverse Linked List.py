
# APPROACH 1: USING ITERATION (BETTER ALGORITHM)


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
    
        p = None
        c = head
        n = c.next
        
        while c != None:
            c.next = p
            p = c
            c = n
            
            if n != None:
                n = n.next
        return p
 """
 T.C : O(N)
 S.C : O(1)
 """
      
# APPROACH 2: USING RECURSION

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverse(head):
            if head.next == None:
                return head
            reverseHead = reverse(head.next)
            
            head.next.next = head
            head.next = None
            
            return reverseHead
        
        if head == None:
            return None
        
        return reverse(head)
      
 """
 T.C: O(N)
 S.C: O(N) { Auxillary Stack Space of Recursion }

 """
