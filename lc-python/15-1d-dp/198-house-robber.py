from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # do we include the previous in the max or do we not? 
        dp = [0]* len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for n in range(2, len(nums)):
            dp[n] = max((nums[n]+dp[n-2]), dp[n-1])

        return dp[-1]
        

class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0,0

        # [r1, r2, n, n+1, ...]
        for n in nums:
            temp = max(n + r1, r2)
            r1 = r2
            r2 = temp

        return r2