
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Greedy - start at the end: 
        n = len(nums)
        target = n-1

        for i in range(n-1,-1,-1):
            max_jump = nums[i]
            if i + max_jump >= target:
                target = i
        
        if 0 == target:
            return True
        return False

        # This is top down DP and it does Time out 
        # n = len(nums)

        # memo = {n-1: True}

        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
        #     # if i == n-1:
        #     #     return True
            
        #     for j in range(1, nums[i] + 1):
        #         # print(j)
        #         if dfs(i+j):
        #             memo[i] = True
        #             return True

        #     memo[i] = False
        #     return False

        # return dfs(0)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n-1

        for i in range(n-1, -1, -1):
            jump = i + nums[i]
            if jump >= goal:
                goal = i
        
        return goal == 0
# The time complexity of this solution is O(n) because we are iterating through the array once.
# The space complexity is O(1) because we are using only a constant amount of extra space to store the target index.
