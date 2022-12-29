"""
https://www.youtube.com/watch?v=CjKJDloMnwE


We will use the concept of binary search. However to find the h-index. If the maximum h-index is present in the list, we return that. 
When maximum h-index is now present in the list, we return the no. of elements after the h-index value which is present in the list.
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
