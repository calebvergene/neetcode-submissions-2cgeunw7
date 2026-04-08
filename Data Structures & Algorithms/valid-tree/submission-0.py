class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree rules:
        # cant have detatched nodes, everything needs to be attatched
        # no cycles

        # make an adjacency list
        adj = collections.defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        # if we havent visited each vertex, then its not a tree
        visited = set()
        cycle = False
        # search for cycles
        def dfs(node, previous):
            # cycle detected!
            if node in visited:
                nonlocal cycle
                cycle = True
                return
            visited.add(node)
            for n in adj[node]:
                if n == previous:
                    continue
                dfs(n, node)
            # return true if traversed whole tree
        
        dfs(0, -1)
        print(cycle)
        return not cycle and len(adj) == len(visited)


        