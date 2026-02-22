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
