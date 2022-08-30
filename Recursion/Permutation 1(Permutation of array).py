#Approach 1: we pop the first element of the array and perform permutation based on the remaining elements
# Source: YT-  Neetcode Permutation I

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
            result.extend(perms)   #appending the perms in result[]
            nums.append(n)       #backtracking. Adding the first element of nums in the end.
            
        return result
      
      """
      T.C:
      S.C:
      
      """

   # Approach 2:
   # Source: YT- Leadcoding by fraz- permutation 1
"""
This question is exactly similar to Permutations - I
Only difference being we have duplicate elements in nums[]. But we need to print Unique Permutations only
For that purpose, we have used a local unordered_set data structure which tells us if that particular element has been previosuly encountered or not
If we have taken / chosen the element before, we will not include it anymore.
But if we haven't included the element, we will include it now
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(pos, n):

            #  Base Case executes when we have traversed the entire nums[]
            if pos >= n:

                ans.append(nums[:])
                return


            for i in range(pos, n):

                # We simply use our swapping logic to create Permutations

                nums[i], nums[pos] = nums[pos], nums[i]

                # And we ask Recursion to handle rest of the task
                helper(pos+1, n)

                # Backtrack and undo the change we have done

                nums[i], nums[pos] = nums[pos], nums[i]
            return

        ans = []


        helper(0, len(nums))

        return ans
