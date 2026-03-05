

""" 
Time Complexity: O(n^2)
Space Complexity: O(1)

The time complexity of this solution is O(n^2) because we are iterating through the string twice 
(once for the outer loop and once for the inner loop). 
The space complexity is O(1) because we are using only a constant amount of extra space to store the variables resIdx and resLen.

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[resIdx : resIdx + resLen]
    
'''
The time complexity of this solution is O(n^2) because we are iterating through the 
string twice (once for the outer loop and once for the inner loop). 
The space complexity is O(1) because we are using only a constant amount of extra space 
to store the variables res and reslen.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        
        res = ""
        reslen = 0

        def helper(i,j):
            # Use nonlocal to modify variables in the outer scope
            nonlocal res, reslen
            l,r = i,j

            while l >= 0 and r < length and s[l] == s[r]:
                if (r-l+1) > reslen:
                    res = s[l:r+1]
                    reslen = r-l +1
                l -= 1
                r += 1
                
        for i in range(length):
            # check the odd case
            helper(i,i)

            # check the even case
            helper(i,i+1)
        
        return res


'''
This approach is similar to the previous one, but instead of using nonlocal variables, 
we directly return the longest palindrome found in the helper function.
The time complexity is still O(n^2) and the space complexity is O(1).
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # We check both centers (i, i) and (i, i+1)
            for l, r in [(i, i), (i, i + 1)]:
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if (r - l + 1) > len(res):
                        res = s[l : r + 1]
                    l -= 1
                    r += 1
        return res
