# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # global has to be an array form to make sure that we can modify it
        # why can't be an int be modified as a global?
        res = [root.val]
        # initialize it to 

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)

            # compute the max path sume with the split 
            res[0] = max(root.val + leftMax + rightMax, res[0])

            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]

