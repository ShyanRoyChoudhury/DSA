""" Approach 1: Using Stack"""


def findMinimumCost(str):
    stack = []
    #odd condition
    if len(str) % 2 != 0:       # if length of string is odd, it is impossible to make it valid
        return -1
    
    for ch in str:
        if ch == '{':
            stack.append(ch)
        else:
            if stack and stack[-1] == '{':      # if the '{}' condition checks out we skip the correct bracket and continue to the next 'invalid bracket'
                stack.pop()
            else:
                stack.append(ch)
    a, b = 0, 0
    while stack:        # a and b represents no of open brackets '{' and closed brackets '}' respectively.
        if stack[-1] == '{':
            a += 1
        else:
            b += 1
        stack.pop()
        
    ans = (a+1)//2 + (b+1)//2
    return int(ans) 
    
