from typing import List

# 45. Jump Game II
# The idea is to use a greedy approach to find the minimum number of jumps needed to reach the end of the array. 
# We maintain two pointers, l and r, which represent the current range of indices that we can jump from. 
# We also keep track of the farthest index we can reach from the current range. 
# We iterate through the current range and update the farthest index we can reach. 
# Once we have processed the current range, we move to the next range defined by l and r, and increment the jump count. 
# We repeat this process until we reach the end of the array.
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # if we're at the end, we have the min jumps which is 0
        #     1 1 0
        # 2,3,1,1,4
        res = 0
        l = r = 0

        while r < n-1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r+1
            r = farthest
            res +=1

        return res
# The time complexity of this solution is O(n) because we are iterating through the array once.
# The space complexity is O(1) because we are using only a constant amount of extra space to store the current left and right indices and the result.
