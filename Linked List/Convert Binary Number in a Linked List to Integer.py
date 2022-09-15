class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        temp = head
        ans = 0
        
        while temp:
            ans *= 2
            ans += temp.val
            temp = temp.next
        
        return ans
      
      
      """
      T.C:  O(N)
      S.C:  O(1)
      """
