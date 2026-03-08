"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        if len(intervals) <= 1:
            return True

        intervals.sort(key=lambda i:i.start)
        for i in range(len(intervals)-1):
            i1 = intervals[i]
            i2 = intervals[i+1]

            if i1.end > i2.start:
                return False
            
        return True

# The time complexity of this solution is O(n log n) because we need to sort the intervals first.
# The space complexity is O(1) because we are sorting the intervals in place and using only 
# a constant amount of extra space to store the current intervals being compared.