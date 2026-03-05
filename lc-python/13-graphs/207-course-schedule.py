
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {i: [] for i in range(numCourses)}
        
        # {1:0,3}, {0:4,5}, etc. 
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # print(preMap)
        
        # this set is for one path of the DFS only
        # must remove from it when done with the path
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True

            visited.add(crs)
            for c in preMap[crs]:
                if not dfs(c): return False

            visited.remove(crs)
            preMap[crs] = []

            return True

        for i in range(numCourses):
            if not (dfs(i)): return False

        return True

