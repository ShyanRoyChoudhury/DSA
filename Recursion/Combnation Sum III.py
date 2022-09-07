"""
This question is exactly similar to Combination Sum -I.
The only difference is that we have duplicates inside the given vector arr[]
We need to skip the duplicate elements. Else they would generate Duplicate Combinations which we don't want
To skip the Duplicate Elements, we will sort arr[] and use a While Loop to skip all the Duplicate Elements

NOTE:
As we haev to pass subset [] and ans [] by it's reference I haven't incuded it in heper() parameter
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(i, k, sum):
            #base condition
            if sum == n:   
                if k == 0:      #  If the sum is equal to n, we include the Subset into our ans[]
                    ans.append(subSet[:])    
                return        
            if sum > n:
                return
            if i > 9:   # since in the question it is mentioned that the range of integers is 0-9
                return
            
            #with ith element
            subSet.append(i)
            sum += i
            helper(i+1, k-1, sum)   # Ask recursion to do the same
            subSet.pop()  # backtracking
            sum -= i      # backtracking
            
            #without ith element
            helper(i+1, k, sum)
        
        sum = 0
        ans = []
        subSet=[]
        helper(1, k, sum)
        
        return ans

"""
Time Complexity: O(2^N)
Space Complexity: O(K)
"""
