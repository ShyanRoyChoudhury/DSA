"""
In this approach, since queue uses FIFO. While pop(): we initially pop the top of queue from the left and append it to the right side of the top of stack(LIFO).
Once this operation is complete we pop the left most element that was initially the top of stack.

link for explanation: https://youtu.be/rW4vm0-DLYc
"""

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q)-1):  #   when using range(N), the loop iterates upto the N - 1. Here range(N - 1) means we iterate upto the final element 
                                        #   which we were initially supossed to remove as per (LIFO). 
            self.push(self.q.popleft())     
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0
      
      
      
"""
T.C : O(N)
S.C : O(N)
"""
