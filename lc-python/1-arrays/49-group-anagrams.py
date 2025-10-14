from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # a dictionary of lists that holds on to the anagrams 

        for s in strs:
            # we want to see how many times each letter appears in a string 
            # this underlying feature will let us see how many strings have the same chars
            # meaning that they're anagrams
            count = [0] * 26 # for alphabet a-z (given constraint)

            for c in s:
                # add the counts of individual alphas into the count of current string
                count[ord(c) - ord('a')] += 1 
            # get the counts for the particular string
            # add it to the resulting hashmap i.e. "eat": 'e':1, 'a':1, 't':1
            # python - you can't store arrays as key but you can tupes (they're immutable)
            res[tuple(count)].append(s)

            # now if anything similar comes up like "ate", it will have the same counts
        return list(res.values())
        
if __name__ == "__main__":
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    Output = [["bat"],["nat","tan"],["ate","eat","tea"]]
    
    res = sol.groupAnagrams(strs)
    print(res)
