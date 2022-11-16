"""
Link: https://www.youtube.com/watch?v=xW4QsTtaCa4
we solve this issue by finding the middle of range. And then using the guess function based on its output to further reduce the scope of search. 
This is very smilar to a binary search algo.

"""

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while True:
            m = (l+r) // 2
            res = guess(m)   #  guess() is predefined in question
            if res > 0:
                l = m+1
            elif res < 0:
                r = m-1
            else:
                return m
              
              
"""
T.C: O(log n)
S.C: O(1)
"""
