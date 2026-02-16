# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True
            
            # The "Global" Check: Is the current node within the allowed range?
            if not (low < node.val < high):
                return False
            
            # When going LEFT: The current node's value is the new HIGH limit
            # When going RIGHT: The current node's value is the new LOW limit
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))

        # Start with the widest possible range
        return validate(root, float('-inf'), float('inf'))