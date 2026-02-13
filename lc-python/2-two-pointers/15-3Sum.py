from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1

            while l < r:
                if (a + nums[l] + nums[r]) < 0:
                    l += 1
                elif (a + nums[l] + nums[r]) > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l +=1
                    while (nums[l] == nums[l-1]) and l < r:
                        l += 1 # we only need to increment one pointer since the if-else takes care 
                        # of the other pointer, we just need to make sure we skip duplicates for the left pointer
        
        return res
    
