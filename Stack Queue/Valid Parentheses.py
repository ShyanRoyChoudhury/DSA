def isValidParenthesis(expression):
    s = []
    # Write your code here.
    for ch in expression: 
        if ch == '(' or ch == '{' or ch == '[':
            s.append(ch)    # Push the element in the stack
        else:
          
            # IF current character is not opening bracket
            # then it must be closing.
            # So stack cannot be empty at this point.
            if not s:
                return False
            current_ch = s.pop()
            if current_ch == '(':
                if ch != ')':
                    return False
            if current_ch == '{':
                if ch != '}':
                    return False
            if current_ch == '[':
                if ch != ']':
                    return False
    if s:
        return False
    
    return True
  
"""
T.C:O(N)
S.C:O(1)
"""
