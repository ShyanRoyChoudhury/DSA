"""
Explanation: https://www.youtube.com/watch?v=RzT6YgrGTyg
"""

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())
        ans = self.s2.pop()

        while self.s2:
            self.s1.append(self.s2.pop())
        return ans

    def peek(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())
        
        ans = self.s2[-1]

        while self.s2:
            self.s1.append(self.s2.pop())
        
        return ans
        
    def empty(self) -> bool:
        return len(self.s1) == 0
      
"""
T.C:O(N)
S.C:
"""
