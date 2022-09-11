"""
This problem asks us to find the Max Length of Concatenated strings present inside arr[]
All the concatenated strings should have unique characters
"""
class Solution:
    def maxLength(self, arr: List[str]) -> int:

        def compare(curString):

            selfCheck = [0 for i in range(26)]

            a = ord("a")

            for i in curString:

                # As all the characters are present in LowerCase, we can use currString[i] - 'a' to map every character to a corresponding index (as discussed thoroughly in the lecture)
                # Here we check if the CurrentString has repeating characters
                if selfCheck[ord(i)-a] == 1:
                    return False
                # Else we mark all the characters inside SelfCheck as 1
                selfCheck[ord(i)-a] = 1

            # The second Loop ensures whether the characters of currString has already been selected or not
            for i in curString:
                if selected[ord(i)-a] == 1:
                    return False

                # At the end, if currString doesn't contain repeating characters AND it's characters have already not been taken yet, we return true indicating currString can be chosen now
            return True

        def helper(i, length):
            # If we reach till the end of arr[], we need to return the max Length we have taken till now
            if i == len(arr):
                return length

            a = ord("a")
            curString = arr[i] #storing each string in curString
            if compare(curString) == False:     # checking for duplicates in curString
                return helper(i+1, length)      # if yes, next string

            # Else we have two options, One to include CurrString OR another option is to Skip CurrString
            else:
                    # Increase the length by currString.size()
                    # pick ith
                for ch in curString:    
                    selected[ord(ch)-a] = 1
                length += len(curString)
                op1 = helper(i + 1, length)     # Ask Recursion to do rest of task
                
                #skip ith
                for j in curString:

                    selected[ord(j)-a] = 0      # backtracking

                # As we are not including currString, we should decrease len by currString.size()
                length -= len(curString)        # backtracking
                op2 = helper(i + 1, length)      # Ask recursion to do rest of the task
                return max(op1, op2)            # Lastly, we will return the max of (op1 , op2) whichever brings the Longest Length

        # G var
        selected = [0 for i in range(26)]

        return helper(0, 0)

"""
Time Complexity:  O(K * 2^N)
Space Complexity: O(N)
"""
