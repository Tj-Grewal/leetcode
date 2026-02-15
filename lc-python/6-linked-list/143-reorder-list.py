# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = 0
        tail = head

        stack = []

        while tail.next:
            tail = tail.next
            mid += 1
        
        middle = int(mid/2)

        curr = head
        i = 0

        while i < middle:
            curr = curr.next # curr is now in the middle of the list
            i += 1

        middi = curr.next
        newTail = curr

        while middi:
            stack.append(middi)
            middi = middi.next
        
        newTail.next = None

        newCurr = head

        while newCurr and stack:
            # hold the temp 1 -> 2  == 2 is temp
            temp = newCurr.next
            # get the last one 4 
            nodeToInsert = stack.pop()
            # 1 -> 4 
            newCurr.next = nodeToInsert
            # 4 -> 2 
            nodeToInsert.next = temp
            newCurr = temp

            
    # TWO ALGOS - 1. Reverse the list from mid point
    #             2. Then merge the two lists from end to mid
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast = head.next
        slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # the middle of the list
        slow.next = None

        prev = None
        #  now reverse the back half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # new tail going backwards is now PREV
        first = head
        second = prev

        while second:
            # save the next for both lists
            t1, t2 = first.next, second.next

            # do the swap, splice in second list node
            first.next = second
            second.next = t1
            
            # update nodes to new nexts for the continuing iteration
            first = t1
            second = t2