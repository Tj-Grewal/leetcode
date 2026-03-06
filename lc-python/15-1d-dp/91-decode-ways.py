class Solution:
    def numDecodings(self, s: str) -> int:
        # initialize the dp array with the last value
        # this sets the key at the length of string to be 1 - base anchor case
        dp = {len(s) : 1}
        
        def dfs(i):
            # if the i exists in the dp
            if i in dp:
                return dp[i]
            if s[i] == "0":
                # we can't make a num with 0 at beginning
                return 0
            
            # we handled what the i case is, now we call next part
            # either we can call it with including i as the num or we want to 
            # combine i and the next num to make it a double digit
            res = dfs(i+1)

            # we make sure we're still in valid index and that it either starts with a 1
            # or a 2. We don't care what follows 1 but for 2 we can only do 0-6
            if (i + 1 < len(s) and (s[i] == "1" or 
                (s[i] == "2" and s[i+1] in "0123456"))):
                res += dfs(i+2)
            
            # don't forget to store the results in the dp array
            dp[i] = res
            return res

        return dfs(0)
    
# The time complexity of this solution is O(n) because in the worst case, we will visit each index of the string once.
# The space complexity is O(n) because in the worst case, we will have to store the results for each index in the dp array.

