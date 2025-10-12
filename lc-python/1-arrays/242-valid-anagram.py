class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return prematurely if the lengths of strings are not the same
        if len(s) != len(t):
            return False

        # Make a hashmap for each
        countS, countT = {}, {}

        for i in range(len(s)):
            # if in the first go the countS[si] doesn't exist on the RHS of = expr,
            # doing the get with 0 makes it a default value, to save syntax failure
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    
if __name__ == "__main__":
    s = "racecar"
    t = "aarrecc"
    sol = Solution()
    val = sol.isAnagram(s,t)
    print(val)
    