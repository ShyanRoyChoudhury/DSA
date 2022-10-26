""" Approach 1: Using Stack"""


def findMinimumCost(str):
    stack = []
    #odd condition
    if len(str) % 2 != 0:
        return -1
    
    for ch in str:
        if ch == '{':
            stack.append(ch)
        else:
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(ch)
    a, b = 0, 0
    while stack:
        if stack[-1] == '{':
            a += 1
        else:
            b += 1
        stack.pop()
        
    ans = (a+1)//2 + (b+1)//2
    return int(ans) 
    
