
# This approach is similar to the Fibonacci sequence, where the number of ways to climb n stairs 
# is the sum of the ways to climb n-1 and n-2 stairs. The time complexity of this solution is O(n) 
# due to the recursive calls and memoization, and the space complexity is O(n) 
# due to the cache used for memoization.
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)

# This approach uses dynamic programming to iteratively build up the solution. 
# The time complexity is O(n) due to the loop, and the space complexity is O(n) due to the dp array.
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    
# This approach optimizes the space complexity to O(1) by only keeping track of the last two values 
# instead of the entire dp array. The time complexity remains O(n).
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
