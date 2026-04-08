class MedianFinder:
    # i think im him
    # so basically, need to heaps: min heap and max heap. 
    # make the max heap less than the min heap
    ## they should always be balancing the same length. 
    ## if one gets to long, remove the root and add it to the other one. 
    

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        ## when adding, need to check which heap to add to then rebalance if needed.

        # empty
        if not self.maxheap and not self.minheap:
            heapq.heappush(self.minheap, num)
            return
        
        # so, will always have an element in the minheap. 
        # add to queue
        if num < self.minheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        
        # rebalance if nessesary
        if len(self.minheap) - len(self.maxheap) >= 2:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        elif len(self.maxheap) - len(self.minheap) >= 2:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))



    def findMedian(self) -> float:
        ## to get the median, return the top node of the longer heap
        if (len(self.maxheap) + len(self.minheap)) % 2 == 0:
            return (-self.maxheap[0] + self.minheap[0])/2
        else:
            # median
            return self.center()
    
    ## new func to get center 
    def center(self) -> int:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            return self.minheap[0]
        
        