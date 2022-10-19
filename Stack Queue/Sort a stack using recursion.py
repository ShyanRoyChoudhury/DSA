def insertStack(stack, num):
    if not stack or stack[-1] < num:
        stack.append(num)
        return
    
    top = stack[-1]
    del stack[-1]
    
    insertStack(stack, num)
    stack.append(top)
    
def sortStack(stack):
    # given data structure is a python list 
    # as list have all the similar operations available so use them
    # Write your code here
    if not stack:
        return
    
    num = stack[-1]
    del stack[-1]
    
    sortStack(stack)
    
    insertStack(stack, num)
