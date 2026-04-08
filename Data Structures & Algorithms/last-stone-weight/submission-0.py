class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ## make max heap
        pq = [-num for num in stones]
        heapq.heapify(pq)

        while len(pq)>1:
            ## have two largest elements
            stone1 = -heapq.heappop(pq)
            stone2 = -heapq.heappop(pq)
            if stone2 == stone1:
                continue
            greater, less = max(stone1, stone2), min(stone1, stone2)
            print(greater, less)
            heapq.heappush(pq, -(greater-less))
        if pq:
            return -pq[0]
        return 0
