"""
Generating Combinations is exactly similar to generating Subsets.
At every stage we will - a) Pick i-th Element
                         b) Don't Pick i-th Element
Instead of giving us an array or vector, we are asked to generate all Combinations from 1 to N (both inclsive) and length of each Subset should be exactly K
We use the same Pick & Don't Pick Logic to solve the Question
We should always remember - Relative order matters in Combination just like Subsets


"""
class Solution(object):
  def combine(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    
    def helper(i, n, k):
      
      #base case
      if k == 0:
        ans.append(subSet[:])
        return
      
      if i > n:
        return
      
      if k > n - i + 1:
        return
      
      #taking ith element
      subSet.append(i)
      helper(i+1, n, k-1)     #asking recursion to do the remaining
      
      subSet.pop()            #backtracking
      
      #skipping the ith element
      
      helper(i+1, n, k)
    
    ans=[]
    subSet=[]
    
    helper(1, n, k)
    return ans
  
  
  """
  Time Complexity  : O(2^N)
  Space Complexity : O(N)
  """
