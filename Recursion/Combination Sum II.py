class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(i, n, sum):
            
            #base condition:
            if sum == target:
                ans.append(subSet[:])
                return
            if sum > target:
                return
            if i==n:
                return
            
           
            
            #taking the ith element
            subSet.append(candidates[i])
            sum += candidates[i]
            helper(i+1, n, sum)
            
            subSet.pop()
            sum -= candidates[i]
            
            
             #skipping the ith element
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            helper(i+1, n, sum)
            
        ans = []
        subSet = []
        sum = 0
        candidates.sort()
        helper(0,len(candidates), sum)
        return ans
