#Approach 1: we pop the first element of the array and perform permutation based on the remaining elements

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        
        #base case
        if len(nums)==1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)         #removing the first element from nums.
            perms=self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)       #backtracking. Adding the first element of nums in the end.
            
        return result
      
      """
      T.C:
      S.C:
      
      """
