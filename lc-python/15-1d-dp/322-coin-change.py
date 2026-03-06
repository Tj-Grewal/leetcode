from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # sort the coins so that we can iterate through them 
        coins.sort()

        # top down dp
        dp = {0:0} # memoize the amounts

        """ 
        [1,4,5]
        0 ways to get to 0, and 1 way to get to sum of 1. 
        But to get to 2 we look at how many ways to get to 2 - 1 = 1 
        Does dp[1] exist in the table? If yes, then how many ways are there? Only 1 way so its 1 + dp[i]
        [0, 1, 2, 3, 4 ]
        """
        def count_coins(amt):
            # always the case with dp, check if we're in the dp
            if amt in dp:
                return dp[amt]
            
            curr = float('inf')
            for c in coins:
                diff = amt - c
                # This is where the sorted order helps. If we're sorted and we know the diff is < 0 at this value, no point checking it further
                if diff < 0:
                    break               
                curr = min(1 + count_coins(diff), curr)
            dp[amt] = curr
            return curr
                
        res = count_coins(amount)
        if res < float('inf'):
            return res
        else:
            return -1
        
# The time complexity of this solution is O(n*m) where n is the amount and m is the number of coins. This is because in the worst case, we will have to check each coin for each amount up to the target amount.
# The space complexity is O(n) because in the worst case, we will have to store the results for each amount up to the target amount in the dp array.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # sort the coins so that we can iterate through them 
        coins.sort()

        # bottom up approach - build the dp array and loop through coins
        dp = [0] * (amount + 1)

        for i in range(1, amount+1):
            curr = float('inf')

            for c in coins:
                diff = i - c
                if diff < 0:
                    break
                curr = min(curr, 1 + dp[diff])
            dp[i] = curr
        
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1