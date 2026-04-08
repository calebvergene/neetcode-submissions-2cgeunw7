class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dykstras algorythm, bfs
        adj = collections.defaultdict(list)
        for time in times:
            adj[time[0]].append((time[2], time[1]))

        # dict of n size, with the time it took to reach each node
        time_to_reach = collections.defaultdict(int)

        # use a heap, all possible movements to nodes 
        heap = [(0, k)]  # (time to reach, node)

        # pop from the heap, read possible nodes to reach that arent in visited
        while heap:
            time, node = heapq.heappop(heap)
            print(time, node)
            if node in time_to_reach:
                continue
            time_to_reach[node] = time
            for next_node in adj[node]:
                if next_node[1] not in time_to_reach:
                    heapq.heappush(heap, (next_node[0] + time, next_node[1]))
        
        # return the max / last element in that dict 
        paths = list(time_to_reach.values())
        return max(paths) if len(paths) == n else -1