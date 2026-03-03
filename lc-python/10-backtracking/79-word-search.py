from types import List

""" 
Time complexity: O(m*4^n) where m is the number of cells in the board and n is the length of the word.
This is because in the worst case, we may have to explore every cell in the board (m) and for each cell, 
we may have to explore up to 4 directions (up, down, left, right) for each character in the word (n).
Space complexity: O(n) where n is the length of the word. This is because in the worst case, 
we may have to explore a path that is as long as the word itself, and we need to store that path in the 
call stack during the depth-first search (DFS) process. 
The maximum depth of the call stack is proportional to n because we can have at most n characters in the word.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLUMNS = len(board), len(board[0])
        path = set()

        def dfs(r,c,i):
            # Did we find every alphabet in word and now we're past it?
            if i == len(word):
                return True
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLUMNS or
                (r,c) in path or
                word[i] != board[r][c]):
                return False
           
            # add the visited path to the path set
            path.add((r,c))

            res = (dfs(r+1, c, i+1)
                    or dfs(r-1, c, i+1)
                    or dfs(r, c+1, i+1)
                    or dfs(r, c-1, i+1))
            path.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLUMNS):
                if dfs(r,c, 0):
                    return True

        return False
