class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # ok, so I need to find a way to detect cycle and then get the edges that are in that cycle. 

        # first make adjacency list 
        adj = collections.defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        # now, dfs through the adj list.
        seen = set()
        cycle = False
        def dfs(node, path, prev): # return true if cycle found
            nonlocal cycle
            path.add(node)
            print(path)
            for nxt in adj[node]:
                if nxt not in seen and nxt != prev and not cycle:
                    # if you find a repeated node in the path then you have a cycle 
                    if nxt in path:
                        path = set() # reset path to backtrack and add nodes in the cycle
                        path.add(nxt)
                        return True 
                    else:
                        cycle = dfs(nxt, path, node)
            # add each node to seen and also track your path. 
            seen.add(node)
            # if no cycle, then dont go back to those nodes because you know there is no cycle 
            if not cycle:
                path.remove(node)
                return False
            else:
                if "end" not in path:
                    if node in path:
                        path.add("end")
                    path.add(node)
                return True


        for node in adj:
            if node not in seen:
                path = set()
                cycle = dfs(node, path, None)
                if cycle:
                    print(path)
                    # then we can return the first one found in og edge list
                    for i in range(len(edges)-1, -1, -1):
                        if edges[i][0] in path and edges[i][1] in path:
                            return edges[i]

                

