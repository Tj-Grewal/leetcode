from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                sum = prices[r] - prices[l]
                profit = max(sum, profit)
            else:
                # if price at R was less then L, move it to the lower price
                l = r 

            r +=1

        return profit
