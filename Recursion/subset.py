class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(i,subset,nums,ans):
            
            #base condition will trigger when the pointer i reaches the end of nums array
            if i==len(nums):
                ans.append(subset[:])
                return
            
            #we include the ith Element
            subset.append(nums[i])
            
            #we ask recursion to do the remaining 
            helper(i+1,subset,nums,ans)
            
            #Backtrack and undo the changes that we made
            subset.pop()
            
            #we dont pick the ith Element
            helper(i+1,subset,nums,ans)
            
        subset=[]
        ans=[]
        
        helper(0, subset, nums, ans)
        
        return ans
      
      
      """
      T.C:
      S.C:
      """
