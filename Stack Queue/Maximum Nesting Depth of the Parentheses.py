class Solution:
    def maxDepth(self, s: str) -> int:
        depth, open = 0, 0
        for i in s:
            if i == '(':
                open += 1
            if i == ')':
                open -= 1
            depth = max(depth, open)
        
        return depth
       
  """
  T.C: O(N)
  S.C: O(1)
  """
