from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1

        for n in nums:
            # 1. Temporarily store the product before curMax changes
            temp_max = curMax * n
            
            # 2. Update curMax using the max of three possibilities
            curMax = max(n, temp_max, curMin * n)
            
            # 3. Update curMin using the min of three possibilities
            curMin = min(n, temp_max, curMin * n)
            
            # 4. Update the global result
            res = max(res, curMax)
            
        return res
# The time complexity of this solution is O(n) because we are iterating through the array once. 
# The space complexity is O(1) because we are using only a constant amount of extra space to store the current maximum and minimum products.