from typing import List
from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0

        """
        Why not just do a dfs on the nodes and if you're already in the set, 
        don't add anything and if you aren't add yourself and continue
        """

        # first build an adj list
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # print(adj)

        visit = set()

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for n in adj[node]:
                dfs(n)
            

        for i in range(n):
            if i in visit:
                visit.remove(i)
            else:
                dfs(i)
                res += 1

        return res

""" 
The time complexity of this solution is O(n + e), where n is the number of nodes and e is the number of edges. This is because we need to build the adjacency list (which takes O(e) time) and then perform a depth-first search (DFS) on each node (which takes O(n + e) time in total, since we visit each node and edge at most once).
The space complexity is O(n + e) as well, due to the adjacency list and the visited set. The adjacency list can take up to O(n + e) space in the worst case (when the graph is dense), and the visited set can take up to O(n) space if all nodes are visited.

"""

# BFS approach
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0

        # first build an adj list
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def bfs(i):
            q = deque([i])
            visit.add(i)
            
            while q:
                node = q.popleft()
                for n in adj[node]:
                    if n not in visit:
                        visit.add(n)
                        q.append(n)
                    """ 
                    if n in visit:
                        continue
                    visit.add(n)
                    q.append(n)
                    """
                    

        for i in range(n):
            if i not in visit:
                bfs(i)
                res+=1
            """ 
            if i in visit:
                continue
            else:
                bfs(i)
                res+=1
            """

        return res
