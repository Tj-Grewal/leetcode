
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []
        preArr = []
        sufArr = [0] * len(nums) # instantiate before hand
        
        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            prefix *= nums[i]
            preArr.append(prefix)
            #[1,2,6,24]
        # print(preArr)

        for i in range(len(nums)-1, -1, -1):
            suffix *= nums[i]
            sufArr[i] = suffix
            # [24,24,12,4]
        # print(sufArr)

        # [1,2,3,4]
        for i in range(len(nums)):
            if i == 0:
                temp = sufArr[i+1]
            elif i == len(nums)-1:
                temp = preArr[i-1]
            else:
                temp = preArr[i-1] * sufArr[i+1]
            result.append(temp)

        return result
