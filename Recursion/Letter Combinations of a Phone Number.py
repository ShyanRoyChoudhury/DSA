class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def  helper(i):
            if i == len(digits):
                new=""
                for j in comb:
                    new += j
                ans.append(new)
                return
            
            for j in range(len(numMap[digits[i]])):
                comb.append(numMap[digits[i]][j])
                
                helper(i+1)
                comb.pop()
        
        comb = []
        ans = []
        numMap = {  "2" : "abc",
                    "3" : "def",
                    "4" : "ghi",
                    "5" : "jkl",
                    "6" : "mno",
                    "7" : "pqrs",
                    "8" : "tuv",
                    "9" : "wxyz"}
        
        if not digits:
            return []
        helper(0)
        return ans
      
      """
      T.C : O(3^n)
      S.C : O(K)
      """
