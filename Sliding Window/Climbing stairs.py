class Solution:
    def climbStairs(self, n: int) -> int:
        if n<1:
            return 
        if n>0 and n<=2:
            return n
        x, y = 1, 2
        for i in range(3, n+1):
            x, y = y, x+y
        return y
      
 """
 T.C: O(N)
 S.C: O(1)
 """
