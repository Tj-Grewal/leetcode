# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        # since it's a binary search tree, we can use the property of the tree to find the lowest common ancestor
        # if both p and q are smaller than the current node, then the lowest common ancestor is in the left subtree
        # if both p and q are larger than the current node, then the lowest common ancestor is in the right subtree
        # if one of p or q is the current node, then the current node is the lowest common ancestor
        # if one of p or q is smaller than the current node and the other is larger than the current node, then the current node is the lowest common ancestor
        # we can use a while loop to traverse the tree until we find the lowest common ancestor
        # the time complexity of this algorithm is O(h) where h is the height of the tree, and the space complexity is O(1) since we are using a constant amount of space
        while curr:
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left 
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            else:
                return curr