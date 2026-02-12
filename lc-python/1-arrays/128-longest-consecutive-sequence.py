from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(list(set(nums)))
        
        temp = 1
        orig = 1

        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                temp +=1 
            else:
                temp = 1
            orig = max(temp, orig)

        return orig