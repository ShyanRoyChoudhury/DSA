def findRedundantBrackets(s:str):
    stack = deque()
    for ch in s:
        if ch in ['(', '+', '-', '*', '/']:
            stack.append(ch)
        else:
            if ch == ')':
                flag = True
                while stack[-1] != '(':
                    if stack[-1] in ['+', '-', '*', '/']:
                        flag = False
                    stack.pop()
                stack.pop()
                if flag == True:
                    return True
    
    return False

  
  
"""
T.C: O(N)
S.C: O(1)
"""
