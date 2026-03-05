
from ast import List

""" 
The time complexity is O(n) where n is the number of nodes in the graph, 
since we visit each node once during the DFS.
The space complexity is also O(n) in the worst case, if the graph is a linear chain, 
as the recursion stack can go as deep as n.

The algorithm works by first building an adjacency list from the given edges. 
Then, it performs a depth-first search (DFS) starting from the first node (0). 

During the DFS, it checks for two conditions:
1. If a node is visited more than once, it means there is a cycle in the graph, 
    and thus it cannot be a valid tree.
2. If the DFS completes without finding a cycle, it checks if all nodes were visited. 
    If all nodes are visited, it means the graph is connected and has no cycles, 
    which confirms that it is a valid tree.

"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
          return True
        if len(edges) > (n - 1):
            return False
        
        # Build the adjacency list by iterating through the edges and adding 
        # each node to the other's list of neighbors.
        # The adjacency list is a dictionary where the keys are node indices and 
        # the values are lists of neighboring nodes.
        # The syntax {i:[] for i in range(n)} creates a dictionary with keys from 0 to n-1,
        # each initialized to an empty list. This is a common way to initialize an adjacency list for a graph with n nodes.
        # For example, if n = 5, this will create the following dictionary:
        # {0: [], 1: [], 2: [], 3: [], 4: []}
        # Then, for each edge [n1, n2], we append n2 to the list of neighbors for n1 and n1 to the list of neighbors for n2,
        # effectively building an undirected graph representation.
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
          adj[n1].append(n2)
          adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
          if i in visit:
            return False

          visit.add(i)
          for j in adj[i]:
            if j == prev:
              continue
            if not dfs(j, i):
              return False
          return True
          
        return dfs(0,-1) and n == len(visit)

from collections import deque
# BFS approach
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        q = deque([(0, -1)])  # (current node, parent node)
        visit.add(0)

        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, node))

        return len(visit) == n