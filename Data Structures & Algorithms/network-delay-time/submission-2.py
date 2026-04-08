class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # use dykstras algorythm
        ## make adjacency list
        adj = collections.defaultdict(list)
        for time in times:
            adj[time[0]].append((time[2], time[1])) # total time, destination
        visited = set()
        total = 0
        pq = [(0, k, 0)]
        while pq and len(visited) < n:
            node = heapq.heappop(pq)
            print(node)
            # make sure haven't already found shortest path for this node
            if node[1] not in visited:
                visited.add(node[1])
                total = max(total, node[0])
                for other in adj[node[1]]:
                    # need to add total distance from source, so:
                    # prev + other time, other node, other time
                    if other[1] not in visited:
                        heapq.heappush(pq, (node[0]+other[0], other[1], other[0]))
        
        return total if len(visited) == n else -1