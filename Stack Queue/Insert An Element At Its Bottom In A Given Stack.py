from os import *
from sys import *
from collections import *
from math import *
def helper(myStack, x):
    if not myStack:
        myStack.append(x)
        return
    top = myStack[-1]
    del myStack[-1]
    
    #recursive call
    helper(myStack, x)
    myStack.append(top)
def pushAtBottom(myStack: deque, x: int):
    helper(myStack, x)
    return myStack
  
  
"""
T.C:O(1)
S.C:O(1)
"""
