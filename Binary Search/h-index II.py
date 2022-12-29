"""
https://www.youtube.com/watch?v=CjKJDloMnwE
"""


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations) 
        left, right = 0, n-1
        while left<=right:
            mid = left + (right-left)//2
            if citations[mid] == n - mid:
                return citations[mid]
            elif citations[mid] > n - mid:
                right = mid - 1
            else:
                left = mid + 1
        return n - left
      
      
      
"""
T.C: O(log n)
S.C: O(1)
"""
