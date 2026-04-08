class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        
        for edge in edges:
            # Check if adding this edge creates a cycle
            if edge[0] in adj and edge[1] in adj:
                # DFS to see if path exists between these nodes
                visited = set()
                def dfs(node, target):
                    if node == target:
                        return True
                    visited.add(node)
                    for neighbor in adj[node]:
                        if neighbor not in visited and dfs(neighbor, target):
                            return True
                    return False
                
                if dfs(edge[0], edge[1]):
                    return edge
            
            # Add edge to adjacency list
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])