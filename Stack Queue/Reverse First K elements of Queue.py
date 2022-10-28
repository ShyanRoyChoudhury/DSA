"""
Approach: Using stacks,

In this approach we get the first k elements from queue and place it in a stack. Since Stack is LIFO, the elements are thus inverted when extracting from stack
and place in back to the same queue. Now we extract and put the elements to maintain the order of elements.
"""

from os import *
from sys import *
from collections import *
from math import *
from queue import LifoQueue

def reverseElements(q, k):
    stack = LifoQueue()
    for i in range(k):
        stack.put(q.get())
    
    while stack.qsize() > 0:
        q.put(stack.get())
    
    n = q.qsize()
    for i in range(n - k):
        q.put(q.get())
        
    return q
  
  
  """
  T.C: O(N)
  S.C: O(1)
  """
