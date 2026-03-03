
from ast import List

"""
Time Complexity: O(2^(t/m)) where t is the target value and m is the minimum value in candidates. 
This is because in the worst case, we can have a combination of numbers that add up to the
target value, and we can either include or exclude each number in the combination. 
The number of combinations is proportional to 2^(t/m) because we can have at most t/m numbers in the combination.
Space Complexity: O(t/m) because in the worst case, we can have a combination of numbers that add up to the target value, 
and we need to store that combination in the call stack during the depth-first search (DFS) process. 
The maximum depth of the call stack is proportional to t/m because we can have at most t/m numbers in the combination.
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # we have to return a list of combinations (not permutations)
        res = []
        candidates.sort()

        def dfs1(i, cur, total):
            if target == total:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
           
            # either add candidate again or not
            cur.append(candidates[i])
            dfs1(i, cur, total+candidates[i])
            cur.pop()
            dfs1(i+1, cur, total)


        def dfs2(i, cur, total):
            if target == total:
                res.append(cur.copy())
                return
           
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    return
                cur.append(candidates[j])
                dfs2(j, cur, total + candidates[j])
                cur.pop()


        dfs2(0,[],0)

        return res