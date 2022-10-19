class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        i = edges[0][0]
        j = edges[0][1]
        if i==edges[1][0] or i == edges[1][1]:
            return i
        if j==edges[1][0] or j == edges[1][1]:
            return j
          
          
"""
T.C:O(1)
S.C:O(1)
"""
