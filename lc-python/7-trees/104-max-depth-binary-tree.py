# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # one liner
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        l = 1 + self.maxDepth(root.left)
        r = 1 + self.maxDepth(root.right)

        res = max(l,r)
        
        return res