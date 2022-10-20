class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def reverseStringhelper(l,r,str):
            if l>=r:
                return
            
            temp = str[l]
            str[l] = str[r]
            str[r] = temp
            
            return reverseStringhelper(l+1,r-1,str)
        
        s = reverseStringhelper(0,len(s)-1,s)
        return
      
      
 """
 T.C: 
 S.C: 
 """


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)
        
        for i in range(len(s)-1):
            s[l], s[r] = s[r], s[l]
        
        return s
    
  
        
        
        
