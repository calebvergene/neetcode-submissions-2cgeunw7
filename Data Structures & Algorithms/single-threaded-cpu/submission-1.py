class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # O(logn) time!
        # use a queue to add to the heap when it is ready to process

        # [enqueue, processing, index]
        for i, task in enumerate(tasks): 
            task.append(i)
        tasks.sort(key=lambda x : -x[0]) # ascending order 

        # each time time is updated, move ready tasks to heap
        order = []
        time = tasks[-1][0]
        heap = []
        while tasks or heap:
            # increment time if you need to "wait" to next task enqueue time 
            if not heap and tasks[-1][0] > time:
                time = tasks[-1][0]
            # start by processing each task that is ready & adding to queue
            while tasks and tasks[-1][0] <= time:
                new_task = tasks.pop()
                heapq.heappush(heap, [new_task[1], new_task[2]]) # [processing, index]
            # next, process the tasks in heap. all tasks in heap are "ready"
            if heap:
                task = heapq.heappop(heap)
                time += task[0]
                order.append(task[1])
        return order
            

            

