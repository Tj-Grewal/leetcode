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

            

        