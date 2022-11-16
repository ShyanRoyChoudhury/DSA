"""
Approach: Bruteforce technique
"""
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
      sec = 0
      i = 0
      while tickets[k] != 0:
        if tickets[i] != 0:
          sec += 1
          tickets[i] -= 1
          
        i = (i+1) % len(tickets)
        
      return sum
    
    
    
"""
Better Approach:
"""
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
      x = tickets[k]
      total = 0
      
      for i in range(len(tickets)):
        if i <= k:
          total += min(x, tickets[i])
          
        else:
          total += min(x-1, tickets[i])
          
      return total
    
"""
T.C: O(N)
S.C: O(1)
"""
