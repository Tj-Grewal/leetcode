
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda i: i[0])
        
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastInt = res[-1][1]

            if start <= lastInt:
                res[-1][1] = max(end, lastInt)
            else:
                res.append([start,end])
        return res

# The time complexity of this solution is O(n log n) because we need to sort the intervals first, 
# and then we iterate through the sorted intervals once. The space complexity is O(n) in the worst case 
# if all intervals are non-overlapping, otherwise it is O(1) if all intervals are overlapping and merged into one interval.
