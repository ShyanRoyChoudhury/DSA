class Solution(object):
    def calPoints(self, ops):
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))

        return sum(stack)
      
  
 """
 T.C: O(N), where N is the length of ops. We parse through every element in the given array once, and do O(1)O(1)O(1) work for each element.
 S.C: O(N), the space used to store our stack
 """
