class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # just have to make sure that there are no cycles in a singular path. 
        adj = collections.defaultdict(list)
        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
        visited = set()
        cycle = False

        # keep track of a path for each iteration
        def dfs(node, path):
            # already visited
            if node in visited:
                return
            # detected a cycle
            if node in path:
                nonlocal cycle
                cycle = True
                return
            
            path.add(node)
            for nxt in adj[node]:
                dfs(nxt, path)
            path.remove(node)
            # this node is cycle free when you get to backtrack part
            visited.add(node)
        
        for node in range(numCourses):
            dfs(node, set())
        
        return not cycle
