from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        islands = 0

        def bfs(r,c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                        nc >= COLUMNS or grid[nr][nc] == "0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"

        def dfs(r,c):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLUMNS or
                "0" == grid[r][c]):
                return
            
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] =="1":
                    bfs(r,c)
                    islands += 1
        
        return islands
                
            
# Time: O(R * C) where R is the number of rows and C is the number of columns in the grid. We visit each cell at most once.
# Space: O(R * C) in the worst case where the grid is filled with land, and the queue (for BFS) or 
# the call stack (for DFS) can grow to hold all land cells.
