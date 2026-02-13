from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1

        res = 0
        # res = (r-l) * (min(height[l], height[r]))

        while l < r:
            area = (r-l) * (min(height[l], height[r]))
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            # elif height[l] > height[r]:
            #     r -=1
            else:
                r -=1 # could remove elif and just make it else instead
                # since both of them are doing the same thing
    
        return res