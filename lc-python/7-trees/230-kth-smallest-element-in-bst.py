# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def build(node):
            if not node:
                return
            
            # 1. Action: Just add the current node I'm standing on
            arr.append(node.val)
            
            # 2. Recurse: Go left, then go right
            build(node.left)
            build(node.right)

        build(root) # This populates 'arr'
        arr.sort()

        return arr[k-1]
    
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            k -= 1
            if 0 == k:
                return curr.val
            curr = curr.right
