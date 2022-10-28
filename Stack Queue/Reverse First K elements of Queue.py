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
