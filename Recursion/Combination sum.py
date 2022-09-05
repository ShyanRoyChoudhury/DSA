class Solution(object):
  def combinationSum(self, candidates, target):
      """
      :type candidates: List[int]
      :type target: int
      :rtype: List[List[int]]
      """
      
      def helper(i, sum):
        # base condition
        if sum == target:
          ans.append(subSet[:])
          return
        if sum > target:    # base condition 2
          return
        if i >= len(candidates):    # base condition 3
          return
        
        # skipping the ith element
        helper(i+1, sum)
        
        sum += candidates[i]    # adding the ith element with sum till now to check base condition
        
        # with the ith element
        subSet.append(candidates[i])  # pushing ith element in the subSet
        helper(i, sum)      # we ask recursion to do the same
        sum -= candidates[i]    # backtracking
        subSet.pop()            # backtracking
      
      ans = []
      subSet = []
      sum = 0
      candidates.sort(reverse = True)
      helper(0, sum)
      return ans
    
    
"""
Time Complexity: O(Exponential) or O(n^2)

Explanation: : As it's very difficult to predict how many children one
particular node can have, evident from the Recursive Tree, as one
element can occur multiple times and also we won't be generating
all the subsets in one go. So, the Time Complexity can be said to be
Exponential only!!


Space Complexity: O(n+m) | n for satck memory and m = size of ans array

Explanation: Space Complexity will be equal to height of the recursive
tree, Which in the worst Case is equal to Target-Sum if we had 1 in
arr[] and we kept on picking only 1 till we reach Target-Sum. That's
why Time complexity is (Target-Sum)
"""
