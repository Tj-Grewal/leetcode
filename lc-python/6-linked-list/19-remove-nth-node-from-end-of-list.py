# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return

        l = head
        r = head

        while n > 0:
            r = r.next
            n -= 1

        if not r: # We ran out the end of the list
            # this means either empty list or list of size 2
            # If the list is [1], returning None is correct
            # if the list is [1,2] returning 2 is correct
            return head.next

        prev = None
        while r:
            r = r.next
            prev = l
            l = l.next

        temp = l.next
        l = prev
        l.next = temp
        
        return head
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # second approach with a dummy node (sentinel)
        dummy = ListNode(0, head) # val is 0 and next is head
        # dummy -> head -> rest of the list

        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next
        return dummy.next
        