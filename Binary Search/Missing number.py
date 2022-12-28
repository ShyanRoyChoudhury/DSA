class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])

        return res
      
      
 """
 T.C:O(n)
 S.C:O(1)
 """
