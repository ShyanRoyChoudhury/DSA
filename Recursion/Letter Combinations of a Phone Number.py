"""
This question requries us to print all Valid Combinations of the given string digits which comprises of digits from 2 to 9.
The only thing we require extra in this question is to map all the letter combinations of the phone number to its corresponding digits.
The rest part of the question remains exactly same

# Hypothesis:
takes digits as input then appends all possible combination of the digits and the maped strings in the particular digit.

digit == string

choice diagraam:
1. 1 char can be choosen only once if it's from one number
2. after choosing 1 char from a digit move i pointer and search for next char in digit and add all combination of the chars in the next dgit.
3. Continue it till i pointer is == len(digits) *********** BASE CASE *************

"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def  helper(i):
            # If i has reached till the end of digits, we have reached a Valid Combination
            # We should include it into ans[][] and return back
            
            # base case
            if i == len(digits):
                new=""              
                # converting the comb [] to a string, then storing it to ans [] | As it'll be more dificult to push and pop() in a string, becuause strings are immutable in python
                for j in comb:
                    new += j
                ans.append(new)
                return
            #  j will take care for the iterating over each chars in numCharMap.values() in a particular key "digit[i]"
            for j in range(len(numMap[digits[i]])):
                comb.append(numMap[digits[i]][j])   # picking the jth char from ith digit from the numCharMap
                
                helper(i+1)      #  Ask recursion to do rest of the task
                comb.pop()       # Backtrack and undo the change we have already done
        
        comb = []
        ans = []
        
        # To solve this question, we need to map all the letters of a particular digit with it's corresponding digit. This is done with the help of a dictionary.
        numMap = {  "2" : "abc",
                    "3" : "def",
                    "4" : "ghi",
                    "5" : "jkl",
                    "6" : "mno",
                    "7" : "pqrs",
                    "8" : "tuv",
                    "9" : "wxyz"}
        
        # As per the problem, for an empty string, we need to return an empty array
        if not digits:
            return []
        helper(0)
        return ans
      
      """
      T.C : O(3^n)
      S.C : O(n)
      """
      
      
