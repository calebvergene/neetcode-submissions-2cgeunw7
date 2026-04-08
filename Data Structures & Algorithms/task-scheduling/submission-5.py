class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # get freqs of each task, 26 possible
        freq = collections.defaultdict(int)
        for task in tasks:
            freq[task] += 1
        
        # now, tasks with higher freq should be processed first using heap

        # the problem is the cooldown. So, we need to use a queue to know 
        # when a task is off cooldown, and then we can add it back to the heap. 
        q = collections.deque()
        heap = [-task for task in freq.values()]
        heapq.heapify(heap)
            
        # so just store the -task so highest freq task processed first. 
        # q represents the next time you can do the task
        # EX: AAABC cooldown = 1
        # A B A C A

        time = 0
        while q or heap:
            if heap: 
                # process avaliable tasks
                task = heapq.heappop(heap)
                if task < -1:
                    # then add back to queue to process cooldown
                    q.append([task+1, time + n])
            if q:
                # see if there is a task that can be added back to heap
                if q[0][1] == time:
                    task = q.popleft()
                    heapq.heappush(heap, task[0])
            time += 1
        
        return time 




        
