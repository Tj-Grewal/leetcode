class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        # if len(s) < len(t):
        #     return ""
        
        
        t_count = {}
        window = {}

        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        # for c in range(len(t)):
        #     t_count[t[c]] = 1 + t_count.get(t[c], 0)
        
        have, need = 0, len(t_count)
        res, resLen = [-1,-1], float("infinity")
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # adding characters to our window map
            if c in t_count and window[c] == t_count[c]:
                have +=1
            
            # checkin if the condition has been met 
            while have == need:
                # update the result
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1

                # pop from the left of our window
                window[s[l]] -= 1

                # its possible that our have and need conditions are out of sync
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
                
        left, right = res
        return s[left: right + 1] if resLen != float("infinity") else ""

        


