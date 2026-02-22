# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: if either array is empty, the tree/subtree is empty
        if not preorder or not inorder:
            return None

        # The first element in preorder is always the root of the current tree
        value = preorder[0]
        root = TreeNode(value)

        # Find the root's position in the inorder array
        # This tells us how many nodes are in the left subtree
        idx = inorder.index(value)

        # Recursively build the left and right subtrees
        root.left = self.buildTree(preorder[1 : idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1 :], inorder[idx + 1 :])

        return root
