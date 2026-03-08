
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return
        if len(intervals) < 2:
            return intervals

        # Sort the intervals by their start time
        intervals.sort(key=lambda i: i[0])
        
        # Initialize the result list with the first interval
        # We will compare each subsequent interval with the last interval in the result list
        res = [intervals[0]]

        for start, end in intervals[1:]:
            # Get the end time of the last interval in the result list
            lastInt = res[-1][1]

            # If the start time of the current interval is less than or equal to the end time of the last interval in the result list,
            # then we have an overlap and we need to merge the intervals by updating the end time of the last interval in the result list to be the maximum of the end time of the current interval and the end time of the last interval in the result list
            if start <= lastInt:
                res[-1][1] = max(end, lastInt)
            else:
                # If there is no overlap, we can simply add the current interval to the result list
                res.append([start,end])
        return res

# The time complexity of this solution is O(n log n) because we need to sort the intervals first, 
# and then we iterate through the sorted intervals once. The space complexity is O(n) in the worst case 
# if all intervals are non-overlapping, otherwise it is O(1) if all intervals are overlapping and merged into one interval.
