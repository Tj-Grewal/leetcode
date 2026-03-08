
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost or len(cost) < 2:
            return 0
        n = len(cost)
        # dp = [float('inf')] * (n) # 1 past cause we want to have another element at the top
        # dp[0] = cost[0]
        # dp[1] = cost[1]
        # # min cost of reaching self is min(cost[i]+ dp[i-1], cost[i] + dp[i-2])
        # for i in range(2, n):
        #     dp[i] = min(cost[i] + dp[i-1], cost[i] + dp[i-2])
        # return min(dp[n-1], dp[n-2]) # return the cost at the very end

        # n = len(cost)
        # memo = {0:0, 1:0}

        # def min_cost(i):
        #     if i in memo:
        #         return memo[i]
        #     else:
        #         memo[i] = min(cost[i-1] + min_cost(i-1),
        #                       cost[i-2] + min_cost(i-2))
        #         return memo[i]
            
        # return min_cost(n)

        prev, curr = 0,0
        for i in range(2, n+1):
            prev, curr = curr, min(cost[i-2] + prev, cost[i-1] + curr)
        
        return curr

# This solution is O(n) time and O(1) space, we can optimize the space by only keeping track of 
# the last two costs instead of the entire dp array.