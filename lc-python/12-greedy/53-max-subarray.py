from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = nums[0]
        curr = 0

        for n in nums:
            if curr < 0:
                curr = 0
            curr += n
            res = max(res, curr)

        return res
                
# The time complexity of this solution is O(n) because we are iterating through the array once.
# The space complexity is O(1) because we are using only a constant amount of extra space to store the current sum and the result.
