
from ast import List


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