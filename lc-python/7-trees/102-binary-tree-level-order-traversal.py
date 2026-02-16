# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        """ 
        This is a standard level order traversal problem, we can use a queue to keep track of the nodes at each level. 
        We can use a while loop to traverse the tree until the queue is empty. At each iteration of the while loop, 
        we can get the number of nodes at the current level by getting the length of the queue. 
        We can then use a for loop to iterate through the nodes at the current level and add their values to a local list. 
        We can also add their left and right children to the queue for the next level. 
        After we have processed all the nodes at the current level, we can add the local list to our result list. 
        Finally, we can return the result list. 
        The time complexity of this algorithm is O(n) where n is the number of nodes in the tree, 
        and the space complexity is O(n) since we are using a queue to store the nodes at each level.
        """
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            local = []
            for i in range(qlen):
                popped = q.popleft()
                if popped:
                    local.append(popped.val)
                    q.append(popped.left)
                    q.append(popped.right)
            if local:
                res.append(local)

        return res
