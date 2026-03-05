from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(numbs):
            r1, r2 = 0,0

            for n in numbs:
                temp = max(n + r1, r2)
                r1 = r2
                r2 = temp
            
            return r2
        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
        
""" 
The time complexity of this solution is O(n) because we are iterating through 
the list of houses twice (once for the first helper function and once for the second helper function). 
The space complexity is O(1) because we are using only a constant amount of extra space to store the variables r1 and r2.

"""

# memoized bottom up solution
class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(numbs):
            if not numbs:
                return 0
            if len(numbs) == 1:
                return numbs[0]

            dp = [0] * len(numbs)
            dp[0] = numbs[0]
            dp[1] = max(numbs[1], numbs[0])

            for i in range(2, len(numbs)):
                dp[i] = max(numbs[i] + dp[i-2], dp[i-1])

            return dp[-1]
        
        if len(nums) == 1:
            return nums[0]

        return max(helper(nums[1:]), helper(nums[:-1]))