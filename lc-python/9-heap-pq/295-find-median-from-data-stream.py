class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        length = len(self.arr)

        if length == 0:
            return
        if length == 1:
            return self.arr[0]
        if length == 2:
            res = self.arr[0] + self.arr[1]
            return res / 2

        mid = len(self.arr) // 2
        if len(self.arr) % 2 == 0:
            return (self.arr[mid-1] + self.arr[mid]) / 2
        else:
            return self.arr[mid]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        n = len(self.arr)

        # clever trick of bitwise operation checking if n is orr or even
        return (self.arr[n // 2] if (n&1) else
                (self.arr[n // 2 -1] + self.arr[n // 2]) / 2)
        

# Most optimal solution is to use two heaps, one min and one max, to keep track of the median in O(log n) time.
# The idea is to maintain the max heap for the smaller half of the numbers and the min heap for the larger half. 
# This way, the median can be easily calculated from the tops of the two heaps.
# The max heap will store the smaller half of the numbers, and the min heap will store the larger half.
# When a new number is added, it is compared to the current median and added to the appropriate heap.
# After adding the number, the heaps are balanced to ensure that their sizes differ by at most one.
# The median can then be calculated based on the sizes of the heaps:
# - If the max heap has more elements, the median is the top of the max heap.
# - If the min heap has more elements, the median is the top of the min heap. 
# - If both heaps have the same number of elements, the median is the average of the tops of both heaps.
# This approach allows for efficient insertion and retrieval of the median, 
# making it suitable for a data stream where numbers are continuously added.
# The time complexity for adding a number is O(log n) due to the heap operations, 
# and the time complexity for finding the median is O(1) since it only involves accessing the tops of the heaps.
# but for inserting a number, we have to do a heap push and possibly a heap pop, which takes O(log n) time.
# The space complexity is O(n) in the worst case, as all numbers could be stored in one of the heaps.
import heapq

class MedianFinder:

    def __init__(self):
        # two heaps, max and min heap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # push the number in the smaller side but make it negative
        # since python doesn't have a max heap - this trick makes 
        # it each number be stored in the opposite order
        # NOTE: Remember to * -1 whenever using the value again
        heapq.heappush(self.small, -1 *num)

        if (self.small and self.large and
            self.small[0]*-1 > self.large[0]):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)
        
        # check if we more in small than large
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return ((self.small[0] * -1) + self.large[0]) / 2
