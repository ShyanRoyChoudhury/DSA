"""
Approach: using stacks, 
Link: https://www.youtube.com/watch?v=qB0zZpBJlh8
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                subStr = ""
                while stack[-1] != '[':   
                    subStr = stack.pop() + subStr   # storing the inner list in a string 
                stack.pop()

                k=""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k     # storing the integer before the inner list in a new variable k

                stack.append(int(k) * subStr)     #

        return "".join(stack)
