"""
Approach: (Greedy)
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): 
            return -1

        balance = 0
        start = 0
        for i in range(len(cost)):  
            balance += (gas[i] - cost[i]) # updating the remaining balance on each index

            if balance < 0: # if true, i.e, not possible to go to next spot.
                balance = 0 # resetting the balance.
                start = i + 1 # checking again from next index

        return start
      
 """
 T.C : O(N)
 S.C : O(N)
 """
