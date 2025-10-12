from typing import List

""" approach:
Two pointers - Left and Right 
the right pointer starts at 0 and the left starts at i 
If the target val is not the val at nums[r] then update 
nums[r] with the value at i, otherwise, skip if it is the target val
this skipping makes it so that the R pointer stays at the index to replace
when we encounter a non target value, we use it to update the target value index ele
This works for continuous approach as by the time you moved i, you're still writing what's
not in the target location: 
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[r] = nums[i]
                r += 1
        return r
    
if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    sol = Solution()
    k = sol.removeElement(nums, val)
    print("Length after removing element:", k)
    print("Modified array:", nums[:k])