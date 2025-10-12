from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # initialize a left pointer that we use to update the array
        l = 1

        """ Approach: 
            Since we want to ignore consecutive similar ints, we can start at index 1
            as index 0 will always be unique. Go through the array, comparing r and r-1 ele
            If they are the same, we keep moving the index but if they aren't the same
            then we place the non-similar R at index L, giving us the unique ele at the point 
            we want. Then we update L and continue the loop
        """
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        
        return l
            

nums = [1, 1, 2, 2, 3]
sol = Solution()
k = sol.removeDuplicates(nums)
print("Length after removing duplicates:", k)
print("Modified array:", nums[:k])