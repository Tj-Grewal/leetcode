class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0

        for r in range(len(s)):
            # the get grabs the value if exists, otherwise gives default 0
            count[s[r]] = 1 + count.get(s[r], 0)
                
            # k is the number of replacements we're allowed
            # so if the length - the max frequency element doesn't fit in window
            # shift the left forward so that it fits. 
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -=1
                l += 1

            res = max(r-l+1, res)
        
        return res
    
# Time: O(n)
# Space: O(1) since we only have 26 characters in the alphabet,
# so the count dictionary will never have more than 26 keys.
