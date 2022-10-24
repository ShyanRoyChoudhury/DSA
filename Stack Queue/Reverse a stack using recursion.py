"""In this approach, we initially pop the first element. 
Then we reverse the stack and then insert the popped element at the bottom of reversed stack."""

def insertAtBottom(stack, num):
        if len(stack) == 0:
            stack.append(num)
            return
        
        top = stack[-1]
        stack.pop()
        insertAtBottom(stack, num)
        stack.append(top)
def reverseStack(stack) :
    
    if len(stack) == 0:
        return
    num = stack.pop()
    reverseStack(stack)
    
    insertAtBottom(stack, num)
    
    
"""
T.C:O(1)
S.C:O(1)
"""
