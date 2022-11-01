"""
Arroach - Using 2 deques,
Link - https://www.youtube.com/watch?v=mUeaCLDdtnM
"""

from os import *
from sys import *
from collections import *
from math import *

def sumOfMaxAndMin(nums, n, k):
    totalSum = 0
    minDQ = []
    maxDQ = []
    
    for i in range(k):
        curr = nums[i]
        
        while len(minDQ) > 0 and nums[minDQ[-1]] >= curr:
            minDQ.pop()
            
        while len(maxDQ) > 0 and nums[maxDQ[-1]] <= curr:
            maxDQ.pop()
            
        minDQ.append(i)
        maxDQ.append(i)
        
    totalSum += (nums[minDQ[0]] + nums[maxDQ[0]])
    
    for i in range(k, n):
        curr = nums[i]
        # removal
        while len(minDQ) > 0 and minDQ[0] <= i - k:
            minDQ.pop(0)
        while len(maxDQ) > 0 and maxDQ[0] <= i - k:
            maxDQ.pop(0)
            
        # addition
        while len(minDQ) > 0 and nums[minDQ[-1]] >= curr:
            minDQ.pop()
            
        while len(maxDQ) > 0 and nums[maxDQ[-1]] <= curr:
            maxDQ.pop()
            
        minDQ.append(i)
        maxDQ.append(i)
        totalSum += (nums[minDQ[0]] + nums[maxDQ[0]])
        
    return totalSum
  
"""
S.C:O(N)
T.C:O(K), where K is the size of the subarray.
Extra space is required for maintaining Dequeues and each Dequeue can have at most K values.
"""
