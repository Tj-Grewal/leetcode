from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        two_sum = dict()

        for i in range(len(nums)):
            # make a key to insert in dict
            new_key = nums[i]
            diff = target - new_key
            if diff in two_sum.keys():
                return two_sum[diff], i
            else:
                two_sum[new_key] = i

if __name__ == "__main__":
    two = Solution()
    num = [2,3,4,5]
    target = 8
    result = two.twoSum(num, target)
    print(result)