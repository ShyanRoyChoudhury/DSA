def deleteMiddle(inputStack, N):

    # Write your solution here
    def helper(inputStack, N, count):
        #base case
        if count == N//2:
            inputStack.pop()
            return
        top = inputStack.pop()
        #Recursive call
        helper(inputStack, N, count+1)
        inputStack.append(top)
     
    helper(inputStack, N, 0)

    
"""
T.C: O(1)
S.C : O(1)
"""
