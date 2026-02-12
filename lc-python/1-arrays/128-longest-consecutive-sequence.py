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
    
    
# Better version - where you only use O(n) time and O(n) space
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Idea is to check if nums-1 exists in set, if not then this is start of sequence
        # then just check if nums+1 exists while maintaining a length counter
        numset = set(nums) # O(N) space complextity
        longest = 0

        for n in numset:
            if (n-1) not in numset:
                length = 0
                while (n + length) in numset:
                    length += 1
                longest = max(length, longest)

        return longest
