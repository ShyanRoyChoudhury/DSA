class Solution:
    def reverse(self, head):
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
        
        while fast.next!= None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next
        
        start = head
        slow.next = self.reverse(slow.next)
        mid = slow.next
        
        
        while mid != None:
            if start.val != mid.val: return False
            
            mid = mid.next
            start = start.next
        #slow.next = self.reversal(slow.next)
        
        return True
