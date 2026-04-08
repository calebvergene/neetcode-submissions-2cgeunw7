class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        
        heap = []
        for num in freq:
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num[1] for num in heap]
        




