"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        # hash map for storing already made nodes 
        nhash = {}

        def dfs(node):
            if node.val in nhash:
                return nhash[node.val]
            else:
                new_node = Node(node.val, [])
                nhash[node.val] = new_node
            for neighbor in node.neighbors:
                print(node.val, neighbor.val)
                nhash[node.val].neighbors.append(dfs(neighbor))
            return new_node
        
        dfs(node)
        return nhash[1]
            
            

