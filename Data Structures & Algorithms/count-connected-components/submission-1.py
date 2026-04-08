class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # components are # of nodes that are seperated. pretty easy lowk
        visited = set()
        components = 0
        # make adjacency list
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # for each iteration, i need to make sure to fully explore the whole graph. 
        # i can do this with bfs so i know i am taking each possible path
        def bfs(n, seen):
            q = collections.deque()
            q.append(n)
            seen.add(n)
            while q:
                node = q.popleft()
                for neighbor in adj[node]:
                    if neighbor not in seen:
                        q.append(neighbor)
                        seen.add(neighbor)
            # while loop ends when we have found each node
            

        # then when iterating each node, I check if i have seen that node before. if not, 
        # ik its a new component, so I call bfs on that. 
        for node in range(n):
            if node not in visited:
                components += 1
                bfs(node, visited)

        # then return the amount of components.
        return components