class Solution:
    ## make method to compute distance
    def distance(self, p1):
        from math import sqrt
        return sqrt((p1[0])**2 + (p1[1])**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_heap = []
        for point in points:
            heapq.heappush(points_heap, (self.distance(point), point))
        k_closest = []
        for i in range(k):
            k_closest.append(heapq.heappop(points_heap)[1])
        return k_closest

