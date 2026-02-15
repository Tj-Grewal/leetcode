
# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    first approach: min heap
    we can use a min heap to always get the smallest head among the k lists
    we push the head of each list into the min heap, and then we pop the smallest one, 
    add it to our result list, 
    and then push the next node from that same list into the min heap (if it exists)
    we repeat this process until the min heap is empty, which means we've processed 
    all the nodes from all the lists
    the time complexity of this approach is O(N log k) where N is the total number of 
    nodes across all lists and k is the number of lists, 
    because we are pushing and popping from the min heap which has a size of at most k
    the space complexity is O(k) because we are storing at most k nodes in the min heap at any time
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        # 1. Initialize: Push the HEAD of every list into the heap
        for i, node in enumerate(lists):
            if node:
                # We use 'i' as the tie-breaker
                heapq.heappush(min_heap, (node.val, i, node))
        
        dummy = ListNode()
        curr = dummy
        
        # 2. Loop: Extract min, add to result, push next
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            
            # Add to your result list
            curr.next = node
            curr = curr.next
            
            # Push the NEXT node from that same list (if it exists)
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        return dummy.next
    
    """ 
    second approach: merge lists in pairs
    we can merge the lists in pairs, which is similar to the merge step in merge sort
    we merge the first two lists, then merge the result with the third list, and
    so on until we've merged all the lists into one
    the time complexity of this approach is O(N log k) where N is the total
    number of nodes across all lists and k is the number of lists, because 
    we are merging pairs of lists log k times and each merge operation takes O(N) time
    the space complexity is O(1) if we don't count the space used for the output list, since we are merging the lists in place
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: 
            return None

        # while we still have lists remaining
        # if lists len becomes 1 then that means they're all merged
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2): # stride of 2 since we want to merge 2 of them
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                result = self.mergeLists(l1, l2)
                mergedLists.append(result)
            lists = mergedLists

        return lists[0]

    def mergeLists(self, l1, l2):
        dummy = ListNode()
        start = dummy

        # edge cases
        if not l1:
            return l2
        if not l2:
            return l1
        
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next

            dummy = dummy.next

        if l1:
            dummy.next = l1
        elif l2:
            dummy.next = l2
        
        return start.next


    """ 
    second approach: divide and conquer
    we can use a divide and conquer approach to merge the lists
    we can divide the lists into two halves, merge each half recursively, and then merge the two halves together
    the time complexity of this approach is O(N log k) where N is the total number of nodes across 
    all lists and k is the number of lists, because we are dividing the lists log k times and each merge operation takes O(N) time
    the space complexity is O(log k) due to the recursive call stack, 
    since we are dividing the lists into halves log k times, the maximum depth of the recursion will be log k
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # second approach: divide and conquer
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        
        return self.mergeTwoLists(left, right)
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
            
        return dummy.next